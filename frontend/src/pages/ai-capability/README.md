# AI Capability Dashboard

This directory contains an interactive product and design prototype for an educator-facing AI capability dashboard inside Frappe Learning.

## Product context

The core idea is not to grade students by school subject or to measure general classroom wellbeing. The product helps a teacher understand **how students work with AI**.

The teacher should be able to:

- see all students in one class at a glance;
- understand each student's current AI capability level;
- observe prompts, model responses, revisions, tool calls, and verification steps;
- open the full task context behind an AI interaction;
- identify patterns that may need coaching;
- distinguish strong AI collaboration from uncritical answer consumption; and
- use the data as evidence for a human coaching decision, not as an automated grade.

The demo is framed as the fictional Northstar Learning Lab and its 25-person Aurora Cohort. All learner records and AI log events are intentionally generic mock data.

## Design direction

The visual direction combines two complementary design-system ideas:

- **Notion-like structure:** calm monochrome workspace chrome, compact navigation, clear hierarchy, document-like information density, and restrained borders.
- **Duolingo-like feedback:** rounded shapes, bright progress colors, tactile buttons, visible momentum, friendly microcopy, and lightweight motion.

Learners are represented as **abstract creature pads, not faces or realistic avatars**. Nine playful silhouettes rotate through the cohort, while each pad is recolored across an 11-step capability scale:

- red: needs coaching;
- yellow: developing; and
- green: AI capable.

The shape provides continuity and personality; the red-to-green color communicates current capability. A small status dot keeps the three headline states scannable. The source assets live in `frontend/public/recolorable-pads/` and can be reused by other product surfaces.

## Current prototype

The registered Vue route is:

```text
/lms/ai-capability
```

Depending on the configured LMS base path, the local Vite URL may be equivalent to `/ai-capability` behind the frontend proxy.

Implemented interactions:

- capability filtering;
- 25-student overview;
- simulated live-log synchronization;
- flagged-session list;
- student context drawer;
- recent AI event timeline; and
- responsive desktop and compact-sidebar layouts.

The page is intentionally self-contained in `AICapabilityDashboard.vue` so the concept can be reviewed before backend schemas and shared components are finalized.

## Capability model represented in the mock data

The current labels cover:

- prompting;
- prompt iteration;
- context building;
- task decomposition;
- reasoning;
- critical evaluation;
- source verification;
- synthesis;
- research strategy;
- tool selection and tool use;
- multimodal creation;
- AI communication;
- AI ethics;
- AI collaboration; and
- agent workflows.

The single capability score in the UI is a placeholder for a future rubric. A production model should retain dimension-level evidence and avoid reducing every learner to one opaque number.

## Suggested data contract

The frontend currently expects a class overview shaped approximately like this:

```ts
type StudentCapabilitySummary = {
	id: string
	name: string
	capabilityScore: number
	focusCapability: string
	capabilityState: 'needs_coaching' | 'developing' | 'ai_capable'
	activeDays: number
	logEventCount: number
	teacherSignal?: string
}
```

A student detail response should add task and log context:

```ts
type StudentAIContext = {
	student: StudentCapabilitySummary
	sessions: Array<{
		id: string
		taskTitle: string
		startedAt: string
		model?: string
		events: Array<{
			type:
				| 'prompt'
				| 'response'
				| 'revision'
				| 'tool_call'
				| 'verification'
			timestamp: string
			content: string
			metadata?: Record<string, unknown>
		}>
	}>
	rubricEvidence: Array<{
		capability: string
		level: number
		evidenceEventIds: string[]
	}>
}
```

## Integration plan

1. Define Frappe doctypes for AI sessions, log events, capability evidence, and teacher signals.
2. Replace the local `students` array with a `createResource` call for a class overview.
3. Load full student context only when the drawer opens.
4. Use the existing Frappe socket connection to stream new log events and update counters.
5. Add role checks so only authorized educators can access identifiable student context.
6. Add retention, consent, audit, and deletion rules before ingesting real student AI activity.
7. Move reusable circle, status, metric, and log components into `frontend/src/components/` after the product model stabilizes.
8. Add unit tests for filtering, capability thresholds, permissions, empty states, and live updates.

## Local development

Use the repository's normal frontend workflow:

```bash
yarn install
yarn dev
```

For a full Frappe-backed environment, follow the root repository setup instructions and open the route through the configured LMS site.

## Important product principles

- AI logs are context, not proof of learning by themselves.
- Capability signals must remain explainable and traceable to evidence.
- Teachers make the final interpretation and coaching decision.
- Students should know what is collected and who can see it.
- Scores should support growth conversations, not surveillance or punitive ranking.
- Real deployments need explicit access controls and data-retention rules.

## Files

- `AICapabilityDashboard.vue` — interactive Vue prototype and mock data
- `README.md` — product intent, design rationale, data contract, and integration plan
- `../../router.js` — route registration
- `../../App.vue` — full-width layout selection for this prototype route
