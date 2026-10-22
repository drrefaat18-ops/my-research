export const meta = {
  name: 'loop-until-dry',
  description: 'Finders run in rounds until K rounds bring nothing new; every fresh find is judged by 3 lenses',
  whenToUse: 'Discovery of unknown size: bugs, gaps, missing citations, edge cases.',
  phases: [
    { title: 'Find', detail: 'finders in parallel each round', model: 'haiku' },
    { title: 'Judge', detail: '3 lenses per fresh find, 2 must confirm', model: 'haiku' },
  ],
}
// args: { finders: [{ key, prompt }], dry_rounds: 2, max_rounds: 6,
//         lenses: ['correctness', 'reproduces', 'in scope'] (optional) }
// Graph: a cycle that converges. Dedupe against everything SEEN (not only confirmed), or rejected finds
// return every round and the loop never runs dry. max_rounds is a hard stop and is logged.

const FOUND = {
  type: 'object', additionalProperties: false,
  properties: { items: { type: 'array', items: {
    type: 'object', additionalProperties: false,
    properties: {
      key: { type: 'string', description: 'stable id, e.g. file:line or a short slug' },
      desc: { type: 'string' },
      evidence: { type: 'string' },
    },
    required: ['key', 'desc', 'evidence'],
  } } },
  required: ['items'],
}
const VERDICT = {
  type: 'object', additionalProperties: false,
  properties: { real: { type: 'boolean' }, reason: { type: 'string' } },
  required: ['real', 'reason'],
}

const { finders = [], dry_rounds = 2, max_rounds = 6, lenses = ['correctness', 'reproduces', 'in scope'] } = args || {}
if (!finders.length) throw new Error('args.finders is empty')

const seen = new Set(), confirmed = [], rejected = []
let dry = 0, round = 0
while (dry < dry_rounds && round < max_rounds) {
  round++
  const known = [...seen].slice(-200).join(', ')
  const found = (await parallel(finders.map((f) => () => agent(
    `${f.prompt}\n\nDo not edit files. Already known (skip these keys): ${known || 'none'}`,
    { label: `find:${f.key}:r${round}`, phase: 'Find', schema: FOUND, model: 'haiku' },
  )))).filter(Boolean).flatMap((r) => r.items)

  const fresh = found.filter((b, i, all) => !seen.has(b.key) && all.findIndex((x) => x.key === b.key) === i)
  if (!fresh.length) { dry++; log(`round ${round}: nothing new (${dry}/${dry_rounds} dry)`); continue }
  dry = 0
  fresh.forEach((b) => seen.add(b.key))

  const judged = await parallel(fresh.map((b) => () => parallel(lenses.map((lens) => () => agent(
    `Judge through the "${lens}" lens only: is this find real? If uncertain, real = false.\n` +
    `FIND ${b.key}: ${b.desc}\nEVIDENCE: ${b.evidence}`,
    { label: `judge:${b.key}:${lens}`, phase: 'Judge', schema: VERDICT, model: 'haiku', effort: 'high' },
  ))).then((v) => ({ b, real: v.filter(Boolean).filter((x) => x.real).length >= 2 }))))
  judged.forEach((j) => (j.real ? confirmed : rejected).push(j.b))
  log(`round ${round}: ${fresh.length} new, ${judged.filter((j) => j.real).length} confirmed`)
}
if (round >= max_rounds && dry < dry_rounds) log(`STOPPED at max_rounds=${max_rounds} before running dry: coverage incomplete`)
return { confirmed, rejected, rounds: round }
