# AGENTS

Scope: this file applies to all work under manim/.

## Repo Identity
- Personal playground for mathematical animations with Manim Community.
- Scratch scenes, experiments, and short explainers. Not a product.

## Jira
- Site: https://macovin.atlassian.net (cloudId `a725ab89-81ab-4178-87dd-9b30306a70dd`)
- Project: `MANIM` (manim) — create in Jira if missing (team-managed software, like HERT/FMS)
- Default issue type: Task
- This project is planned backlog-first: epics, stories, and tasks are
  drafted and approved in chat, then created in `To Do`. Don't start
  sprints, assign people, or move tickets unless asked. Building happens one
  ticket at a time when someone picks it up.
- Company or factory work goes in `MAC` or `MNWL`; link counterparts both
  ways.

## Stack
- Python 3.9+ with a local `.venv`
- Manim Community (`manim`), not ManimGL, unless a ticket says otherwise
- ffmpeg is required for video renders (already on this machine)
- No TeX yet: prefer `Text` over `MathTex` until a ticket installs LaTeX

## Working Rules for Agents
- Scenes live under `scenes/`, one module per topic or experiment.
- Prefer small, re-renderable scenes over long multi-scene films.
- Render with quality flags explicitly (`-ql` while iterating, `-qh` when polishing).
- Media output (`media/`) is gitignored; never commit rendered videos or caches.
- Don't invent math claims in narration. If a scene teaches something, the math in the scene is the source of truth.
- Use `meanwhile-ticket-loop` for setup and tooling tickets. Play sessions that aren't ticketed stay local until you ask to capture them.
