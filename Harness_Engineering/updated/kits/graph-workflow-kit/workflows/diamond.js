export const meta = {
  name: 'diamond',
  description: 'Fan out one cheap agent per item, reduce in code, optional synthesis by one stronger agent',
  whenToUse: 'Many independent items (sources, files, routes) that need the same job, then one merged answer.',
  phases: [
    { title: 'Fan out', detail: 'one agent per item', model: 'haiku' },
    { title: 'Synthesize', detail: 'one agent over the deduped set', model: 'sonnet' },
  ],
}
// args: { task: '{{what each agent does to its item}}', items: [{ key: 'a', input: '{{path or text}}' }],
//         synthesize: '{{optional: what the final agent writes from all findings}}' }
// Graph: split (args) -> fan out (cheap) -> barrier + reduce (code, 0 tokens) -> synthesize (one agent, optional).

const FINDINGS = {
  type: 'object', additionalProperties: false,
  properties: {
    findings: { type: 'array', items: {
      type: 'object', additionalProperties: false,
      properties: {
        title: { type: 'string' },
        detail: { type: 'string' },
        evidence: { type: 'string', description: 'verbatim quote, file:line, or URL' },
      },
      required: ['title', 'detail', 'evidence'],
    } },
    unreadable: { type: 'array', items: { type: 'string' } },
  },
  required: ['findings', 'unreadable'],
}

const { task, items = [], synthesize } = args || {}
if (!task || !items.length) throw new Error('args.task and args.items are required')

phase('Fan out')
const raw = await parallel(items.map((it) => () => agent(
  `${task}\n\nYour item (${it.key}):\n${it.input}\n\nDo not edit files. A failed read goes in unreadable, never guessed.`,
  { label: `item:${it.key}`, phase: 'Fan out', schema: FINDINGS, model: 'haiku', effort: 'low' },
)))

// Barrier is justified: dedupe needs the whole set.
const dead = items.filter((_, i) => !raw[i]).map((it) => it.key)
if (dead.length) log(`no result (re-run): ${dead.join(', ')}`)
const seen = new Map()
raw.forEach((r, i) => r && r.findings.forEach((f) => {
  const k = f.title.trim().toLowerCase()
  if (!seen.has(k)) seen.set(k, { ...f, from: [items[i].key] })
  else seen.get(k).from.push(items[i].key)
}))
const findings = [...seen.values()]
const unreadable = raw.filter(Boolean).flatMap((r) => r.unreadable).concat(dead)
log(`${findings.length} unique findings from ${items.length - dead.length}/${items.length} items`)

if (!synthesize || !findings.length) return { findings, unreadable }

phase('Synthesize')
const report = await agent(
  `${synthesize}\n\nUse only these findings; cite each by its evidence.\n${JSON.stringify(findings)}`,
  { label: 'synthesize', phase: 'Synthesize', model: 'sonnet' },
)
return { findings, unreadable, report }
