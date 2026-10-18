export const meta = {
  name: 'skeptic-panel',
  description: 'Each claim faces N cheap skeptics with different lenses; it survives only with a majority',
  whenToUse: 'Before a human reviews generated claims, findings or sentences.',
  phases: [{ title: 'Verify', detail: 'one agent per claim per lens, vote in code', model: 'haiku' }],
}
// args: { claims: [{ id: 1, text: '...', evidence: ['quote or file:line', ...] }],
//         lenses: [{ key, ask }] (optional, defaults below), need: 2 (optional) }
// Graph: per claim fan out to distinct lenses -> vote in code. Diverse lenses catch what N identical checks miss.

const VERDICT = {
  type: 'object', additionalProperties: false,
  properties: { refuted: { type: 'boolean' }, reason: { type: 'string' } },
  required: ['refuted', 'reason'],
}
const DEFAULT_LENSES = [   // {{replace with the ways a claim can be wrong in this project}}
  { key: 'evidence', ask: 'Every number, name and fact in the claim appears in the evidence with the same value.' },
  { key: 'scope', ask: 'The evidence is about the same thing, case and audience as the claim.' },
  { key: 'overreach', ask: 'The claim says no more than the evidence: no stronger wording, generalisation or added cause.' },
]

const { claims = [], lenses = DEFAULT_LENSES } = args || {}
const need = (args && args.need) || Math.floor(lenses.length / 2) + 1
if (!claims.length) throw new Error('args.claims is empty')

phase('Verify')
const rows = await parallel(claims.map((c) => () => parallel(lenses.map((lens) => () => agent(
  [
    'Do not read, create or edit any file. Judge only from the text below.',
    `Your one lens (${lens.key}): ${lens.ask}`,
    'Try to refute the claim. If you are uncertain, refuted = true. One-line reason.',
    `CLAIM ${c.id}: ${c.text}`,
    'EVIDENCE:', ...(c.evidence || []).map((e) => `- ${e}`),
  ].join('\n'),
  { label: `skeptic:${c.id}:${lens.key}`, phase: 'Verify', schema: VERDICT, model: 'haiku', effort: 'high' },
))).then((votes) => {
  const cast = votes.map((v, i) => v && { lens: lenses[i].key, ...v }).filter(Boolean)
  if (cast.length < lenses.length) log(`claim ${c.id}: ${lenses.length - cast.length} lens(es) returned nothing`)
  return { id: c.id, text: c.text, survives: cast.filter((v) => !v.refuted).length >= need, votes: cast }
})))

const killed = rows.filter((r) => r && !r.survives).map((r) => r.id)
log(`${rows.length - killed.length}/${rows.length} survive (need ${need}/${lenses.length}); refuted: ${killed.join(', ') || 'none'}`)
return rows
