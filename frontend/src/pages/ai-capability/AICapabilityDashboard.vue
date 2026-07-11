<template>
	<div class="ai-shell">
		<aside class="ai-sidebar">
			<div class="ai-wordmark">
				<span class="mark"><i></i><i></i></span>
				<strong>AI Capability</strong>
			</div>
			<button class="class-switch">
				<span class="class-icon">10A</span>
				<span
					><strong>Class 10A</strong><small>Ms. Berg · 25 students</small></span
				>
				<b>⌄</b>
			</button>
			<nav aria-label="AI capability navigation">
				<label>TODAY</label>
				<a class="active" href="#ai-overview"
					><span>◉</span>AI overview<kbd>1</kbd></a
				>
				<a href="#student-contexts"><span>●</span>Students<kbd>25</kbd></a>
				<a href="#live-logs"><span>⌁</span>AI logs<kbd>47</kbd></a>
				<label>INTELLIGENCE</label>
				<a href="#context-review"><span>▤</span>Context review</a>
				<a href="#capability-rubric"><span>✦</span>Capability rubric</a>
			</nav>
			<div class="sidebar-footer">
				<div class="sync-card">
					<span>↻</span>
					<p>
						<strong>47 new AI logs</strong
						><small>Synced across 25 students</small>
					</p>
				</div>
				<button>
					<span>MB</span>
					<p><strong>Ms. Berg</strong><small>AI learning coach</small></p>
					<i>•••</i>
				</button>
			</div>
		</aside>

		<main class="ai-main" id="ai-overview">
			<header class="ai-topbar">
				<div>
					<span>STANFORD HIGH SCHOOL</span><i>/</i
					><strong>AI capability · Class 10A</strong>
				</div>
				<div class="top-actions">
					<span class="live"><i></i> LOGS LIVE</span
					><button class="more" aria-label="More options">•••</button
					><button class="sync-button" @click="syncLogs">
						↻&nbsp; SYNC AI LOGS
					</button>
				</div>
			</header>

			<div class="ai-content">
				<section class="hero">
					<div>
						<span>STANFORD HIGH SCHOOL · 47 AI LOGS IN THE LAST 20 MIN</span>
						<h1>How is Class 10A working with AI?</h1>
						<p>
							Every student’s AI activity, capability signals, and full working
							context in one view.
						</p>
					</div>
					<div class="growth">
						<i>✦</i><b>+7%</b><small>AI capability this week</small>
					</div>
				</section>

				<section class="metrics" aria-label="AI capability metrics">
					<div>
						<span class="metric green">✓</span>
						<p>
							<strong>{{ capableCount }} AI capable</strong
							><small>verify and iterate independently</small>
						</p>
						<b>↑ 2</b>
					</div>
					<div>
						<span class="metric yellow">↗</span>
						<p>
							<strong>{{ developingCount }} developing</strong
							><small>building reliable AI habits</small>
						</p>
						<b>→</b>
					</div>
					<div>
						<span class="metric red">!</span>
						<p>
							<strong>{{ coachingCount }} need coaching</strong
							><small>review their AI context first</small>
						</p>
						<b>↓ 1</b>
					</div>
					<div class="average">
						<span
							class="ring"
							:style="{ '--score': `${averageScore * 3.6}deg` }"
							><b>{{ averageScore }}</b
							><small>%</small></span
						>
						<p>
							<strong>AI capability</strong
							><small>class-wide readiness score</small>
						</p>
					</div>
				</section>

				<div class="dashboard-grid">
					<section class="map-card" id="student-contexts">
						<div class="card-head">
							<div>
								<span>AI CAPABILITY MAP</span>
								<h2>25 student contexts at a glance</h2>
							</div>
							<div class="filters">
								<button
									:class="{ active: filter === 'all' }"
									@click="filter = 'all'"
								>
									All</button
								><button
									:class="{ active: filter === 'coaching' }"
									@click="filter = 'coaching'"
								>
									Needs coaching</button
								><button
									:class="{ active: filter === 'capable' }"
									@click="filter = 'capable'"
								>
									AI capable
								</button>
							</div>
						</div>
						<div class="dot-field">
							<div class="log-note">
								<span>⌁</span>
								<p>
									<strong>47 new AI logs</strong
									><small>activity updates live</small>
								</p>
							</div>
							<div class="orbit orbit-one"></div>
							<div class="orbit orbit-two"></div>
							<button
								v-for="student in visibleStudents"
								:key="student.id"
								class="student-node"
								:aria-label="`${student.name}, ${statusFor(student.score).label}, ${student.score}%`"
								@click="selected = student"
							>
								<span
									class="student-dot"
									:class="`tone-${statusFor(student.score).tone}`"
									:style="{ '--dot': student.color }"
									><i></i><b></b
								></span>
								<strong>{{ student.name }}</strong
								><small>{{ student.score }}% · {{ student.capability }}</small>
							</button>
							<div class="teacher-card">
								<span>MB</span>
								<p><strong>Ms. Berg</strong><small>AI learning coach</small></p>
								<i>All student contexts are live</i>
							</div>
						</div>
						<div class="legend">
							<span><i class="red"></i>needs coaching</span
							><span><i class="yellow"></i>developing</span
							><span><i class="green"></i>AI capable</span
							><small
								>Status dot shows AI capability · circle color identifies each
								student</small
							>
						</div>
					</section>

					<aside class="right-rail">
						<section class="activity-card" id="live-logs">
							<span>LIVE AI ACTIVITY</span>
							<div class="radar"><i></i><i></i><i></i><b>47</b></div>
							<h3>Review student AI logs</h3>
							<p>
								See every prompt, response, revision, tool call, and teacher
								signal with full task context.
							</p>
							<button @click="showToast('Opening live AI activity')">
								OPEN LIVE AI LOGS <span>→</span>
							</button>
							<small>47 NEW · LAST 20 MIN</small>
						</section>
						<section class="review-card" id="context-review">
							<div class="review-head">
								<span
									><small>SESSIONS TO REVIEW</small
									><strong>{{ coachingCount }} student contexts</strong></span
								><button aria-label="View flagged sessions">→</button>
							</div>
							<button
								v-for="student in coachingStudents"
								:key="student.id"
								class="review-row"
								@click="selected = student"
							>
								<span
									class="mini-dot"
									:style="{ '--dot': student.color }"
								></span>
								<p>
									<strong>{{ student.name }}</strong
									><small>{{ student.note }}</small>
								</p>
								<b>›</b>
							</button>
						</section>
						<section class="signal-card">
							<span>💡</span>
							<p>
								<strong>Capability signal</strong
								><small>Maya now verifies sources without a reminder</small>
							</p>
							<button aria-label="Dismiss signal">×</button>
						</section>
					</aside>
				</div>
			</div>

			<footer>
				<span>Stanford High School · AI capability prototype</span>
				<p>
					AI activity and full task context are visible to authorized educators.
				</p>
				<span>Logs synced 10:24 AM</span>
			</footer>
		</main>

		<div v-if="selected" class="drawer-backdrop" @click.self="selected = null">
			<aside class="student-drawer">
				<button
					class="drawer-close"
					aria-label="Close student context"
					@click="selected = null"
				>
					×
				</button>
				<div class="drawer-dot">
					<span
						class="student-dot large"
						:class="`tone-${statusFor(selected.score).tone}`"
						:style="{ '--dot': selected.color }"
						><i></i><b></b></span
					><em :class="statusFor(selected.score).tone">{{
						statusFor(selected.score).label
					}}</em>
				</div>
				<h2>{{ selected.name }}</h2>
				<p class="drawer-meta">
					Focus: {{ selected.capability }} · {{ logCount(selected) }} AI log
					events today
				</p>
				<div class="level">
					<div>
						<span>AI capability score</span
						><strong>{{ selected.score }}%</strong>
					</div>
					<p>
						<i
							:style="{
								width: `${selected.score}%`,
								background: selected.color,
							}"
						></i>
					</p>
				</div>
				<blockquote>“{{ selected.note }}”</blockquote>
				<div class="drawer-stats">
					<div>
						<span>AI sessions</span
						><strong>{{ selected.streak + 2 }} this week</strong>
					</div>
					<div>
						<span>Capability trend</span
						><strong>+{{ Math.max(2, selected.streak) }}%</strong>
					</div>
				</div>
				<section class="context-log">
					<header><span>RECENT AI CONTEXT</span><b>Live</b></header>
					<p>
						<i>✓</i
						><span
							><strong>Output challenged</strong
							><small>Asked AI to explain a weak assumption</small></span
						><time>10:18</time>
					</p>
					<p>
						<i>↗</i
						><span
							><strong>{{ selected.capability }} activity</strong
							><small>Added context and refined the request</small></span
						><time>10:12</time>
					</p>
					<p>
						<i class="warn">!</i
						><span
							><strong>Teacher signal</strong
							><small
								>{{ statusFor(selected.score).label }} pattern detected</small
							></span
						><time>10:04</time>
					</p>
				</section>
				<button
					class="open-context"
					@click="showToast(`Opening ${selected.name}'s full AI context`)"
				>
					OPEN FULL AI CONTEXT <span>→</span>
				</button>
				<small class="privacy"
					>Demo AI activity · visible to authorized educators</small
				>
			</aside>
		</div>
		<div class="toast" :class="{ show: toast }">
			{{ toastMessage }} <span>✓</span>
		</div>
	</div>
</template>

<script setup>
import { computed, ref } from 'vue'

const students = ref([
	{
		id: 1,
		name: 'Maya',
		score: 91,
		capability: 'Source verification',
		streak: 6,
		note: 'Checks citations before using an AI answer.',
		color: '#58cc02',
	},
	{
		id: 2,
		name: 'Leo',
		score: 48,
		capability: 'Critical evaluation',
		streak: 1,
		note: 'Often accepts the first AI response without testing it.',
		color: '#ff5d5d',
	},
	{
		id: 3,
		name: 'Aylin',
		score: 76,
		capability: 'Prompt iteration',
		streak: 3,
		note: 'Refines prompts when the first result is too broad.',
		color: '#2bb5f5',
	},
	{
		id: 4,
		name: 'Noah',
		score: 35,
		capability: 'Task decomposition',
		streak: 0,
		note: 'Needs help breaking a complex task into AI-ready steps.',
		color: '#ff4b4b',
	},
	{
		id: 5,
		name: 'Sofia',
		score: 95,
		capability: 'Tool selection',
		streak: 8,
		note: 'Chooses tools strategically and explains why.',
		color: '#8b5cf6',
	},
	{
		id: 6,
		name: 'Ethan',
		score: 64,
		capability: 'Context building',
		streak: 2,
		note: 'Adds useful context but still misses key constraints.',
		color: '#ffc800',
	},
	{
		id: 7,
		name: 'Zara',
		score: 82,
		capability: 'AI collaboration',
		streak: 5,
		note: 'Uses AI as a thinking partner, not an answer machine.',
		color: '#ff8a35',
	},
	{
		id: 8,
		name: 'Finn',
		score: 57,
		capability: 'Prompting',
		streak: 1,
		note: 'Writes clear requests but rarely follows up.',
		color: '#ffb020',
	},
	{
		id: 9,
		name: 'Amara',
		score: 88,
		capability: 'Synthesis',
		streak: 4,
		note: 'Combines multiple AI outputs into one coherent view.',
		color: '#1cb0f6',
	},
	{
		id: 10,
		name: 'Ben',
		score: 71,
		capability: 'Reasoning',
		streak: 3,
		note: 'Asks AI to show its reasoning and checks key steps.',
		color: '#ce82ff',
	},
	{
		id: 11,
		name: 'Chloe',
		score: 84,
		capability: 'AI communication',
		streak: 7,
		note: 'Turns AI drafts into clear, original writing.',
		color: '#ff86d0',
	},
	{
		id: 12,
		name: 'Diego',
		score: 53,
		capability: 'Source verification',
		streak: 1,
		note: 'Needs a repeatable process for checking AI claims.',
		color: '#ff7043',
	},
	{
		id: 13,
		name: 'Elena',
		score: 79,
		capability: 'Research strategy',
		streak: 5,
		note: 'Uses AI to map a topic before deeper research.',
		color: '#00b8a9',
	},
	{
		id: 14,
		name: 'Gabriel',
		score: 68,
		capability: 'Context building',
		streak: 2,
		note: 'Progressing with examples, roles, and constraints.',
		color: '#ffc800',
	},
	{
		id: 15,
		name: 'Hana',
		score: 93,
		capability: 'Agent workflows',
		streak: 9,
		note: 'Builds reliable multi-step workflows and reviews outputs.',
		color: '#58cc02',
	},
	{
		id: 16,
		name: 'Isaac',
		score: 46,
		capability: 'Reasoning',
		streak: 0,
		note: 'Lets AI make decisions without challenging assumptions.',
		color: '#ff5d5d',
	},
	{
		id: 17,
		name: 'Jade',
		score: 74,
		capability: 'Prompt iteration',
		streak: 3,
		note: 'One step away from a consistent iteration habit.',
		color: '#2bb5f5',
	},
	{
		id: 18,
		name: 'Kai',
		score: 86,
		capability: 'Critical evaluation',
		streak: 6,
		note: 'Actively challenges weak or unsupported AI outputs.',
		color: '#8b5cf6',
	},
	{
		id: 19,
		name: 'Liam',
		score: 61,
		capability: 'Prompting',
		streak: 2,
		note: 'Gets better results when using a prompt framework.',
		color: '#ffb020',
	},
	{
		id: 20,
		name: 'Mei',
		score: 90,
		capability: 'Multimodal creation',
		streak: 7,
		note: 'Combines text, image, and data tools thoughtfully.',
		color: '#00b8a9',
	},
	{
		id: 21,
		name: 'Nora',
		score: 66,
		capability: 'AI ethics',
		streak: 2,
		note: 'Recognizes bias but needs to document decisions.',
		color: '#ff86d0',
	},
	{
		id: 22,
		name: 'Owen',
		score: 43,
		capability: 'Source verification',
		streak: 0,
		note: 'Uses unverified AI facts in final work.',
		color: '#ff4b4b',
	},
	{
		id: 23,
		name: 'Priya',
		score: 81,
		capability: 'Tool use',
		streak: 5,
		note: 'Selects tools well and documents her process.',
		color: '#1cb0f6',
	},
	{
		id: 24,
		name: 'Sam',
		score: 72,
		capability: 'Synthesis',
		streak: 4,
		note: 'Summarizes well but should preserve source nuance.',
		color: '#ce82ff',
	},
	{
		id: 25,
		name: 'Theo',
		score: 87,
		capability: 'Agent workflows',
		streak: 6,
		note: 'Monitors multi-step tasks and recovers from errors.',
		color: '#ff8a35',
	},
])

const filter = ref('all')
const selected = ref(null)
const toast = ref(false)
const toastMessage = ref('AI logs synced')

const statusFor = (score) =>
	score < 55
		? { label: 'Needs coaching', tone: 'red' }
		: score < 75
			? { label: 'Developing', tone: 'yellow' }
			: { label: 'AI capable', tone: 'green' }
const capableCount = computed(
	() => students.value.filter((student) => student.score >= 75).length,
)
const coachingCount = computed(
	() => students.value.filter((student) => student.score < 55).length,
)
const developingCount = computed(
	() => students.value.length - capableCount.value - coachingCount.value,
)
const averageScore = computed(() =>
	Math.round(
		students.value.reduce((total, student) => total + student.score, 0) /
			students.value.length,
	),
)
const coachingStudents = computed(() =>
	students.value.filter((student) => student.score < 55),
)
const visibleStudents = computed(() =>
	students.value.filter(
		(student) =>
			filter.value === 'all' ||
			(filter.value === 'coaching' ? student.score < 55 : student.score >= 75),
	),
)
const logCount = (student) => 5 + student.streak * 3 + (student.id % 5)

let toastTimer
function showToast(message) {
	toastMessage.value = message
	toast.value = true
	clearTimeout(toastTimer)
	toastTimer = setTimeout(() => (toast.value = false), 2200)
}
function syncLogs() {
	students.value = students.value.map((student, index) => ({
		...student,
		score: Math.min(
			98,
			Math.max(28, student.score + ((student.score + index) % 7) - 3),
		),
	}))
	showToast('AI logs synced')
}
</script>

<style scoped>
* {
	box-sizing: border-box;
}
.ai-shell {
	--ink: #242424;
	--muted: #787774;
	--line: #e6e5e2;
	--green: #58cc02;
	--green-dark: #46a302;
	--yellow: #ffc800;
	--red: #ff4b4b;
	display: flex;
	min-height: 100vh;
	background: #fff;
	color: var(--ink);
	font-family: Inter, ui-sans-serif, system-ui, sans-serif;
}
.ai-shell button {
	font: inherit;
	color: inherit;
	cursor: pointer;
}
.ai-sidebar {
	position: sticky;
	top: 0;
	z-index: 10;
	display: flex;
	width: 248px;
	height: 100vh;
	flex: 0 0 auto;
	flex-direction: column;
	border-right: 1px solid var(--line);
	background: #f7f7f5;
	padding: 18px 12px 14px;
}
.ai-wordmark {
	display: flex;
	align-items: center;
	gap: 9px;
	padding: 2px 8px 16px;
	font-size: 14px;
}
.mark {
	position: relative;
	display: block;
	width: 27px;
	height: 27px;
	transform: rotate(-2deg);
	border: 2px solid #242424;
	border-radius: 8px;
	background: #fff;
	box-shadow: 0 2px 0 #242424;
}
.mark i {
	position: absolute;
	top: 7px;
	left: 5px;
	width: 7px;
	height: 7px;
	border-radius: 50%;
	background: var(--green);
}
.mark i + i {
	top: 11px;
	right: 5px;
	left: auto;
	background: var(--yellow);
}
.class-switch {
	display: flex;
	width: 100%;
	align-items: center;
	gap: 9px;
	border: 1px solid var(--line);
	border-radius: 10px;
	background: #fff;
	padding: 9px;
	text-align: left;
	box-shadow: 0 1px 2px #00000008;
}
.class-switch > span:nth-child(2) {
	flex: 1;
}
.class-icon {
	display: grid;
	width: 31px;
	height: 31px;
	place-items: center;
	border-radius: 9px;
	background: #d9f7c6;
	color: #3f8d12;
	font-size: 10px;
	font-weight: 850;
}
.class-switch strong,
.class-switch small {
	display: block;
}
.class-switch strong {
	font-size: 11px;
}
.class-switch small {
	margin-top: 2px;
	color: #94928f;
	font-size: 8px;
}
.class-switch > b {
	color: #aaa;
	font-size: 11px;
}
.ai-sidebar nav {
	padding-top: 18px;
}
.ai-sidebar nav label {
	display: block;
	padding: 12px 9px 7px;
	color: #a3a19d;
	font:
		700 8px ui-monospace,
		monospace;
	letter-spacing: 0.1em;
}
.ai-sidebar nav a {
	display: flex;
	height: 34px;
	align-items: center;
	gap: 10px;
	margin: 1px 0;
	border-radius: 7px;
	padding: 0 9px;
	color: #6f6d69;
	font-size: 11px;
	text-decoration: none;
}
.ai-sidebar nav a:hover,
.ai-sidebar nav a.active {
	background: #ebebe8;
	color: #242424;
}
.ai-sidebar nav a.active {
	font-weight: 650;
}
.ai-sidebar nav a > span {
	width: 15px;
	text-align: center;
}
.ai-sidebar nav a.active > span {
	color: var(--green-dark);
}
.ai-sidebar nav kbd {
	display: grid;
	min-width: 18px;
	height: 18px;
	place-items: center;
	margin-left: auto;
	border: 0;
	border-radius: 5px;
	background: #dfdfdc;
	color: #777570;
	font:
		8px ui-monospace,
		monospace;
}
.sidebar-footer {
	margin-top: auto;
}
.sync-card {
	display: flex;
	align-items: center;
	gap: 9px;
	margin: 12px 5px;
	border: 1px solid #dcebcf;
	border-radius: 10px;
	background: #f2ffe9;
	padding: 11px;
}
.sync-card > span {
	font-size: 18px;
	color: var(--green-dark);
}
.sync-card p,
.sidebar-footer > button p {
	margin: 0;
}
.sync-card strong,
.sync-card small,
.sidebar-footer > button strong,
.sidebar-footer > button small {
	display: block;
}
.sync-card strong,
.sidebar-footer > button strong {
	font-size: 10px;
}
.sync-card small,
.sidebar-footer > button small {
	margin-top: 2px;
	color: #7e9171;
	font-size: 8px;
}
.sidebar-footer > button {
	display: flex;
	width: 100%;
	align-items: center;
	gap: 9px;
	border: 0;
	border-radius: 8px;
	background: transparent;
	padding: 8px;
	text-align: left;
}
.sidebar-footer > button > span {
	display: grid;
	width: 29px;
	height: 29px;
	place-items: center;
	border-radius: 8px;
	background: #242424;
	color: #fff;
	font-size: 9px;
	font-weight: 800;
}
.sidebar-footer > button p {
	flex: 1;
}
.sidebar-footer > button i {
	color: #aaa;
	font-style: normal;
}
.ai-main {
	display: flex;
	min-width: 0;
	min-height: 100vh;
	flex: 1;
	flex-direction: column;
}
.ai-topbar {
	position: sticky;
	top: 0;
	z-index: 8;
	display: flex;
	height: 61px;
	flex: 0 0 auto;
	align-items: center;
	justify-content: space-between;
	border-bottom: 1px solid var(--line);
	background: #ffffffee;
	padding: 0 30px;
	backdrop-filter: blur(15px);
}
.ai-topbar > div:first-child {
	display: flex;
	align-items: center;
	gap: 9px;
	font-size: 10px;
}
.ai-topbar > div:first-child span {
	border-radius: 5px;
	background: #f0f0ed;
	padding: 4px 6px;
	font-size: 8px;
	font-weight: 750;
}
.ai-topbar > div:first-child i {
	color: #bbb;
	font-style: normal;
}
.top-actions {
	display: flex;
	align-items: center;
	gap: 9px;
}
.live {
	margin-right: 5px;
	color: #74716d;
	font:
		700 8px ui-monospace,
		monospace;
	letter-spacing: 0.08em;
}
.live i {
	display: inline-block;
	width: 7px;
	height: 7px;
	margin-right: 6px;
	border-radius: 50%;
	background: var(--green);
	box-shadow: 0 0 0 4px #58cc021f;
	animation: pulse 2s infinite;
}
.more {
	display: grid;
	width: 32px;
	height: 32px;
	place-items: center;
	border: 1px solid var(--line);
	border-radius: 8px;
	background: #fff;
	color: #888;
	font-size: 11px;
}
.sync-button,
.activity-card > button,
.open-context {
	border: 0;
	border-bottom: 4px solid var(--green-dark);
	border-radius: 11px;
	background: var(--green);
	color: #fff;
	padding: 9px 13px 7px;
	font-size: 9px;
	font-weight: 850;
	letter-spacing: 0.035em;
}
.ai-content {
	width: min(1430px, 100%);
	margin: 0 auto;
	padding: 38px clamp(24px, 4vw, 64px) 48px;
}
.hero {
	display: flex;
	align-items: flex-end;
	justify-content: space-between;
	gap: 24px;
	margin-bottom: 26px;
}
.hero > div:first-child > span,
.card-head > div > span,
.activity-card > span {
	color: #9b9893;
	font:
		700 8px ui-monospace,
		monospace;
	letter-spacing: 0.12em;
}
.hero h1 {
	margin: 8px 0 7px;
	font-size: clamp(30px, 3.5vw, 48px);
	line-height: 1.03;
	letter-spacing: -0.055em;
}
.hero p {
	margin: 0;
	color: var(--muted);
	font-size: 12px;
}
.growth {
	position: relative;
	display: flex;
	width: 150px;
	height: 82px;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	border: 1px solid #e0e9d8;
	border-radius: 16px;
	background: #f4ffec;
	box-shadow: 0 3px 0 #d8e9cc;
}
.growth i {
	position: absolute;
	top: 11px;
	left: 17px;
	color: var(--yellow);
	font-style: normal;
}
.growth b {
	color: var(--green-dark);
	font-size: 24px;
}
.growth small {
	color: #6f8d5b;
	font-size: 8px;
}
.metrics {
	display: grid;
	grid-template-columns: repeat(3, 1fr) 1.15fr;
	overflow: hidden;
	margin-bottom: 18px;
	border: 1px solid var(--line);
	border-radius: 14px;
}
.metrics > div {
	display: flex;
	min-height: 82px;
	align-items: center;
	gap: 11px;
	border-right: 1px solid var(--line);
	padding: 16px 18px;
}
.metrics > div:last-child {
	border: 0;
}
.metric {
	display: grid;
	width: 37px;
	height: 37px;
	place-items: center;
	border-radius: 11px;
	font-weight: 900;
}
.metric.green {
	background: #e7f9d9;
	color: #48a408;
}
.metric.yellow {
	background: #fff5c7;
	color: #b68d00;
}
.metric.red {
	background: #ffe3e3;
	color: #e23d3d;
}
.metrics p {
	flex: 1;
	margin: 0;
}
.metrics p strong,
.metrics p small {
	display: block;
}
.metrics p strong {
	font-size: 11px;
}
.metrics p small {
	margin-top: 3px;
	color: #989692;
	font-size: 8px;
}
.metrics > div > b {
	color: #999;
	font:
		700 9px ui-monospace,
		monospace;
}
.average {
	background: #fafaf8;
}
.ring {
	--score: 0deg;
	position: relative;
	display: grid;
	width: 45px;
	height: 45px;
	place-items: center;
	border-radius: 50%;
	background: conic-gradient(var(--green) var(--score), #e7e7e3 0);
}
.ring:before {
	position: absolute;
	inset: 5px;
	border-radius: 50%;
	background: #fafaf8;
	content: '';
}
.ring b,
.ring small {
	position: relative;
	z-index: 1;
}
.ring b {
	font-size: 13px;
}
.ring small {
	margin-left: -4px;
	font-size: 6px;
}
.dashboard-grid {
	display: grid;
	grid-template-columns: minmax(650px, 1fr) 300px;
	align-items: start;
	gap: 18px;
}
.map-card,
.activity-card,
.review-card,
.signal-card {
	border: 1px solid var(--line);
	border-radius: 14px;
	background: #fff;
}
.map-card {
	overflow: hidden;
}
.card-head {
	display: flex;
	min-height: 72px;
	align-items: center;
	justify-content: space-between;
	gap: 16px;
	border-bottom: 1px solid var(--line);
	padding: 17px 20px;
}
.card-head h2 {
	margin: 4px 0 0;
	font-size: 17px;
	letter-spacing: -0.03em;
}
.filters {
	display: flex;
	border-radius: 8px;
	background: #f4f4f1;
	padding: 3px;
}
.filters button {
	border: 0;
	border-radius: 6px;
	background: transparent;
	padding: 6px 9px;
	color: #8c8985;
	font-size: 8px;
}
.filters button.active {
	background: #fff;
	color: #242424;
	font-weight: 700;
	box-shadow: 0 1px 3px #00000014;
}
.dot-field {
	position: relative;
	display: grid;
	min-height: 695px;
	grid-template-columns: repeat(5, minmax(90px, 1fr));
	align-content: start;
	gap: 31px 10px;
	overflow: hidden;
	background-color: #fbfbf9;
	background-image: radial-gradient(#e4e4df 1px, transparent 1px);
	background-size: 22px 22px;
	padding: 92px 22px 132px;
}
.dot-field:before,
.dot-field:after {
	position: absolute;
	border-radius: 50%;
	content: '';
}
.dot-field:before {
	top: -130px;
	right: -140px;
	width: 330px;
	height: 330px;
	background: #effbe7;
}
.dot-field:after {
	bottom: -120px;
	left: -140px;
	width: 250px;
	height: 250px;
	background: #fff7d8;
}
.log-note {
	position: absolute;
	top: 24px;
	left: 24px;
	z-index: 3;
	display: flex;
	align-items: center;
	gap: 9px;
	transform: rotate(-1deg);
	border: 1px solid var(--line);
	border-radius: 11px;
	background: #fff;
	padding: 10px 12px;
	box-shadow: 0 3px 0 #e8e8e4;
}
.log-note > span {
	color: var(--green-dark);
}
.log-note p {
	margin: 0;
}
.log-note strong,
.log-note small {
	display: block;
}
.log-note strong {
	font-size: 9px;
}
.log-note small {
	margin-top: 2px;
	color: #999;
	font-size: 7px;
}
.orbit {
	position: absolute;
	z-index: 1;
	border: 3px dashed #e1e1dc;
	border-radius: 50%;
}
.orbit-one {
	top: 110px;
	left: 16%;
	width: 470px;
	height: 280px;
	transform: rotate(-8deg);
}
.orbit-two {
	right: -3%;
	bottom: -30px;
	width: 340px;
	height: 220px;
	transform: rotate(12deg);
}
.student-node {
	position: relative;
	z-index: 4;
	display: flex;
	min-width: 0;
	flex-direction: column;
	align-items: center;
	border: 0;
	background: transparent;
	padding: 0;
}
.student-node:hover .student-dot {
	transform: translateY(-5px) scale(1.05);
}
.student-node > strong {
	margin-top: 7px;
	font-size: 10px;
}
.student-node > small {
	max-width: 100%;
	overflow: hidden;
	margin-top: 2px;
	color: #979590;
	font-size: 7px;
	text-overflow: ellipsis;
	white-space: nowrap;
}
.student-dot {
	--dot: #58cc02;
	position: relative;
	display: block;
	width: 57px;
	height: 57px;
	transition: 0.22s;
	border: 4px solid #fff;
	border-radius: 50%;
	background: var(--dot);
	box-shadow:
		0 0 0 3px color-mix(in srgb, var(--dot) 32%, #ddd),
		0 7px 0 color-mix(in srgb, var(--dot) 72%, #333),
		0 10px 18px #2020201f;
}
.student-dot > i {
	position: absolute;
	top: 15%;
	left: 20%;
	width: 28%;
	height: 18%;
	transform: rotate(-22deg);
	border-radius: 50%;
	background: #ffffff61;
}
.student-dot > b {
	position: absolute;
	top: -5px;
	right: -7px;
	width: 8px;
	height: 8px;
	border: 2px solid #fff;
	border-radius: 50%;
	background: var(--green);
}
.student-dot.tone-red > b {
	background: var(--red);
}
.student-dot.tone-yellow > b {
	background: var(--yellow);
}
.student-dot.large {
	width: 112px;
	height: 112px;
	border-width: 7px;
}
.teacher-card {
	position: absolute;
	bottom: 22px;
	left: 50%;
	z-index: 5;
	display: grid;
	width: 310px;
	grid-template-columns: 38px 1fr auto;
	align-items: center;
	gap: 9px;
	transform: translateX(-50%);
	border: 2px solid #292929;
	border-bottom-width: 5px;
	border-radius: 14px;
	background: #fff;
	padding: 10px 12px;
}
.teacher-card > span {
	display: grid;
	width: 38px;
	height: 38px;
	place-items: center;
	border-radius: 10px;
	background: #242424;
	color: #fff;
	font-size: 10px;
	font-weight: 800;
}
.teacher-card p {
	margin: 0;
}
.teacher-card strong,
.teacher-card small {
	display: block;
}
.teacher-card strong {
	font-size: 10px;
}
.teacher-card small {
	margin-top: 2px;
	color: #94918d;
	font-size: 7px;
}
.teacher-card > i {
	border-radius: 7px;
	background: #f7f7f5;
	padding: 7px 8px;
	color: #555;
	font:
		italic 9px Georgia,
		serif;
	white-space: nowrap;
}
.legend {
	display: flex;
	min-height: 44px;
	align-items: center;
	gap: 14px;
	border-top: 1px solid var(--line);
	padding: 0 18px;
	color: #76736f;
	font-size: 8px;
}
.legend span {
	display: flex;
	align-items: center;
	gap: 5px;
}
.legend i {
	width: 7px;
	height: 7px;
	border-radius: 50%;
}
.legend i.red {
	background: var(--red);
}
.legend i.yellow {
	background: var(--yellow);
}
.legend i.green {
	background: var(--green);
}
.legend small {
	margin-left: auto;
	color: #aaa8a3;
	font-size: 7px;
}
.right-rail {
	display: flex;
	flex-direction: column;
	gap: 14px;
}
.activity-card {
	position: relative;
	overflow: hidden;
	border-color: #dfeeda;
	background: #f7ffef;
	padding: 20px;
	text-align: center;
}
.radar {
	position: relative;
	display: grid;
	width: 94px;
	height: 94px;
	place-items: center;
	margin: 15px auto 14px;
	border-radius: 50%;
	background: #dcf8c8;
}
.radar > i {
	position: absolute;
	width: 54px;
	height: 9px;
	transform: rotate(28deg);
	border: 2px solid #8ed457;
	border-radius: 9px;
	background: #fff;
}
.radar > i:nth-child(2) {
	transform: rotate(90deg);
}
.radar > i:nth-child(3) {
	transform: rotate(150deg);
}
.radar > b {
	position: relative;
	z-index: 2;
	display: grid;
	width: 43px;
	height: 43px;
	place-items: center;
	border: 4px solid #fff;
	border-radius: 50%;
	background: var(--green);
	color: #fff;
	box-shadow: 0 4px 0 var(--green-dark);
	font-size: 14px;
}
.activity-card h3 {
	margin: 0;
	font-size: 18px;
}
.activity-card p {
	max-width: 220px;
	margin: 8px auto 16px;
	color: #72806a;
	font-size: 9px;
	line-height: 1.55;
}
.activity-card > button {
	width: 100%;
	text-align: left;
}
.activity-card > button span,
.open-context span {
	float: right;
}
.activity-card > small {
	display: block;
	margin-top: 9px;
	color: #8aa27b;
	font:
		7px ui-monospace,
		monospace;
}
.review-card {
	overflow: hidden;
}
.review-head {
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding: 16px;
}
.review-head span small,
.review-head span strong {
	display: block;
}
.review-head span small {
	color: #999;
	font:
		700 8px ui-monospace,
		monospace;
	letter-spacing: 0.1em;
}
.review-head span strong {
	margin-top: 4px;
	font-size: 15px;
}
.review-head button {
	display: grid;
	width: 32px;
	height: 32px;
	place-items: center;
	border: 1px solid var(--line);
	border-radius: 8px;
	background: #fff;
}
.review-row {
	display: flex;
	width: 100%;
	align-items: center;
	gap: 10px;
	border: 0;
	border-top: 1px solid var(--line);
	background: #fff;
	padding: 12px 15px;
	text-align: left;
}
.mini-dot {
	width: 29px;
	height: 29px;
	flex: 0 0 auto;
	border: 3px solid #fff;
	border-radius: 50%;
	background: var(--dot);
	box-shadow:
		0 0 0 2px color-mix(in srgb, var(--dot) 30%, #ddd),
		0 4px 0 color-mix(in srgb, var(--dot) 72%, #333);
}
.review-row p {
	min-width: 0;
	flex: 1;
	margin: 0;
}
.review-row strong,
.review-row small {
	display: block;
}
.review-row strong {
	font-size: 10px;
}
.review-row small {
	overflow: hidden;
	margin-top: 3px;
	color: #9c9995;
	font-size: 7px;
	text-overflow: ellipsis;
	white-space: nowrap;
}
.review-row > b {
	color: #aaa;
	font-size: 18px;
}
.signal-card {
	display: flex;
	align-items: center;
	gap: 9px;
	border-color: #ede3c5;
	background: #fff9df;
	padding: 12px;
}
.signal-card > span {
	display: grid;
	width: 30px;
	height: 30px;
	place-items: center;
	border-radius: 9px;
	background: #fff;
}
.signal-card p {
	flex: 1;
	margin: 0;
}
.signal-card strong,
.signal-card small {
	display: block;
}
.signal-card strong {
	font-size: 9px;
}
.signal-card small {
	margin-top: 2px;
	color: #8d8467;
	font-size: 7px;
}
.signal-card button {
	border: 0;
	background: none;
	color: #aaa;
}
.ai-main > footer {
	display: flex;
	height: 44px;
	align-items: center;
	justify-content: space-between;
	border-top: 1px solid var(--line);
	padding: 0 30px;
	color: #aaa7a2;
	font:
		7px ui-monospace,
		monospace;
}
.ai-main > footer p {
	margin: 0;
}
.drawer-backdrop {
	position: fixed;
	inset: 0;
	z-index: 50;
	background: #18181645;
	backdrop-filter: blur(4px);
}
.student-drawer {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	width: min(420px, 100%);
	overflow: auto;
	background: #fff;
	padding: 28px;
	box-shadow: -20px 0 60px #00000026;
}
.drawer-close {
	position: absolute;
	top: 18px;
	right: 18px;
	display: grid;
	width: 32px;
	height: 32px;
	place-items: center;
	border: 1px solid var(--line);
	border-radius: 8px;
	background: #fff;
	font-size: 18px;
}
.drawer-dot {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 35px 0 22px;
}
.drawer-dot em {
	margin-top: 23px;
	border-radius: 20px;
	padding: 5px 9px;
	font:
		normal 700 7px ui-monospace,
		monospace;
	letter-spacing: 0.07em;
}
.drawer-dot em.green {
	background: #e7f9d9;
	color: #3f9204;
}
.drawer-dot em.yellow {
	background: #fff2b8;
	color: #997700;
}
.drawer-dot em.red {
	background: #ffe0e0;
	color: #d43636;
}
.student-drawer h2 {
	margin: 0;
	text-align: center;
	font-size: 34px;
	letter-spacing: -0.05em;
}
.drawer-meta {
	margin: 5px 0 23px;
	color: #8d8a85;
	font-size: 9px;
	text-align: center;
}
.level {
	border-top: 1px solid var(--line);
	border-bottom: 1px solid var(--line);
	padding: 18px 0;
}
.level > div {
	display: flex;
	align-items: flex-end;
	justify-content: space-between;
}
.level > div span {
	color: #85827e;
	font-size: 9px;
}
.level > div strong {
	font-size: 20px;
}
.level > p {
	height: 9px;
	overflow: hidden;
	margin: 11px 0 0;
	border-radius: 8px;
	background: #ededeb;
}
.level > p i {
	display: block;
	height: 100%;
	border-radius: 8px;
}
.student-drawer blockquote {
	margin: 18px 0;
	border-left: 3px solid #c9c8c4;
	border-radius: 0 9px 9px 0;
	background: #f7f7f5;
	padding: 15px;
	color: #55514c;
	font:
		italic 14px/1.5 Georgia,
		serif;
}
.drawer-stats {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 9px;
	margin-bottom: 17px;
}
.drawer-stats div {
	border: 1px solid var(--line);
	border-radius: 9px;
	padding: 12px;
}
.drawer-stats span,
.drawer-stats strong {
	display: block;
}
.drawer-stats span {
	color: #9b9893;
	font-size: 7px;
}
.drawer-stats strong {
	margin-top: 4px;
	font-size: 11px;
}
.context-log {
	overflow: hidden;
	margin-bottom: 16px;
	border: 1px solid var(--line);
	border-radius: 11px;
}
.context-log header {
	display: flex;
	height: 37px;
	align-items: center;
	justify-content: space-between;
	border-bottom: 1px solid var(--line);
	background: #f7f7f5;
	padding: 0 12px;
}
.context-log header span {
	color: #85827e;
	font:
		700 7px ui-monospace,
		monospace;
	letter-spacing: 0.1em;
}
.context-log header b {
	color: var(--green-dark);
	font-size: 8px;
}
.context-log p {
	display: grid;
	min-height: 49px;
	grid-template-columns: 22px 1fr auto;
	align-items: center;
	gap: 8px;
	margin: 0;
	border-bottom: 1px solid var(--line);
	padding: 9px 11px;
}
.context-log p:last-child {
	border: 0;
}
.context-log p > i {
	display: grid;
	width: 21px;
	height: 21px;
	place-items: center;
	border-radius: 6px;
	background: #e7f9d9;
	color: #419900;
	font-size: 9px;
	font-style: normal;
	font-weight: 800;
}
.context-log p > i.warn {
	background: #fff1c7;
	color: #a57d00;
}
.context-log p > span strong,
.context-log p > span small {
	display: block;
}
.context-log p > span strong {
	font-size: 8px;
}
.context-log p > span small {
	margin-top: 2px;
	color: #9a9792;
	font-size: 7px;
}
.context-log time {
	color: #aaa;
	font:
		7px ui-monospace,
		monospace;
}
.open-context {
	width: 100%;
	text-align: left;
}
.privacy {
	display: block;
	margin-top: 10px;
	color: #aaa;
	font-size: 7px;
	text-align: center;
}
.toast {
	position: fixed;
	bottom: 20px;
	left: 50%;
	z-index: 80;
	transform: translate(-50%, 30px);
	opacity: 0;
	border-radius: 10px;
	background: #242424;
	padding: 11px 14px;
	color: #fff;
	box-shadow: 0 10px 28px #0003;
	font-size: 9px;
	pointer-events: none;
	transition: 0.25s;
}
.toast.show {
	transform: translate(-50%, 0);
	opacity: 1;
}
.toast span {
	margin-left: 9px;
	color: #7ee33d;
}
@keyframes pulse {
	50% {
		transform: scale(0.72);
		opacity: 0.55;
	}
}
@media (max-width: 1150px) {
	.dashboard-grid {
		grid-template-columns: 1fr;
	}
	.right-rail {
		display: grid;
		grid-template-columns: 1fr 1fr;
	}
	.signal-card {
		grid-column: 1/-1;
	}
	.metrics {
		grid-template-columns: 1fr 1fr;
	}
	.metrics > div:nth-child(2) {
		border-right: 0;
	}
	.metrics > div:nth-child(-n + 2) {
		border-bottom: 1px solid var(--line);
	}
}
@media (max-width: 780px) {
	.ai-sidebar {
		width: 68px;
		padding: 14px 8px;
	}
	.ai-wordmark {
		justify-content: center;
		padding-inline: 0;
	}
	.ai-wordmark strong,
	.class-switch > span:nth-child(2),
	.class-switch > b,
	.ai-sidebar nav a:not(.active),
	.ai-sidebar nav label,
	.sync-card,
	.sidebar-footer > button p,
	.sidebar-footer > button i {
		display: none;
	}
	.class-switch,
	.sidebar-footer > button {
		justify-content: center;
	}
	.ai-sidebar nav a.active {
		justify-content: center;
		padding: 0;
	}
	.ai-sidebar nav kbd {
		display: none;
	}
	.ai-content {
		padding: 25px 16px 40px;
	}
	.ai-topbar {
		padding: 0 16px;
	}
	.live,
	.more {
		display: none;
	}
	.growth {
		display: none;
	}
	.metrics {
		grid-template-columns: 1fr 1fr;
	}
	.dot-field,
	.card-head,
	.legend {
		min-width: 660px;
	}
	.map-card {
		overflow: auto;
	}
	.right-rail {
		grid-template-columns: 1fr;
	}
	.signal-card {
		grid-column: auto;
	}
	.ai-main > footer p {
		display: none;
	}
}
@media (prefers-reduced-motion: reduce) {
	*,
	*:before,
	*:after {
		animation-duration: 0.001ms !important;
		animation-iteration-count: 1 !important;
		transition-duration: 0.001ms !important;
	}
}
</style>
