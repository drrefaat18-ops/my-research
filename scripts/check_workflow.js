// Runs a workflow script against stub agents: catches syntax errors, bad args handling and broken
// reduce code without spending a token. Each stub agent returns a value built from its schema.
// Usage: node check_workflow.js .claude/workflows/<name>.js '<args json>'
const fs = require('fs')

const [file, argsJson = '{}'] = process.argv.slice(2)
if (!file) { console.error('usage: node check_workflow.js <workflow.js> [args json]'); process.exit(2) }

function fake(schema) {   // smallest value that satisfies a JSON schema
  if (!schema) return 'stub text'
  if (schema.enum) return schema.enum[0]
  switch (schema.type) {
    case 'object': return Object.fromEntries(Object.entries(schema.properties || {}).map(([k, s]) => [k, fake(s)]))
    case 'array': return schema.items ? [fake(schema.items)] : []
    case 'integer': case 'number': return 1
    case 'boolean': return false
    default: return 'stub'
  }
}

const calls = []
const agent = async (prompt, opts = {}) => {
  if (typeof prompt !== 'string' || !prompt.trim()) throw new Error(`empty prompt (${opts.label})`)
  calls.push(`${opts.label || 'agent'}:${opts.model || 'NO MODEL'}`)
  return fake(opts.schema)
}
const parallel = (thunks) => Promise.all(thunks.map((t) => t().catch(() => null)))
const pipeline = (items, ...stages) => Promise.all(items.map(async (item, i) => {
  let r = item
  for (const s of stages) { try { r = await s(r, item, i) } catch { return null } }
  return r
}))
const body = fs.readFileSync(file, 'utf8').replace(/^export const meta/m, 'const meta')
const run = new Function('args', 'agent', 'parallel', 'pipeline', 'phase', 'log', 'budget',
  `return (async () => {\n${body}\n})()`)
const budget = { total: null, spent: () => 0, remaining: () => Infinity }

run(JSON.parse(argsJson), agent, parallel, pipeline, () => {}, (m) => console.log('log:', m), budget)
  .then((out) => {
    const noModel = calls.filter((c) => c.endsWith('NO MODEL'))
    console.log(`${calls.length} agent call(s): ${[...new Set(calls)].join(', ')}`)
    console.log('result:', JSON.stringify(out).slice(0, 300))
    if (noModel.length) { console.log('FAIL: agent() without model'); process.exit(1) }
    console.log('ok')
  })
  .catch((e) => { console.log('FAIL:', e.message); process.exit(1) })
