# manim

Personal playground for [Manim Community](https://www.manim.community/) — math animations in the 3Blue1Brown style.

## Setup

Needs Homebrew `cairo` + `pkg-config` (and Python 3.12+).

```bash
brew install cairo pkg-config python@3.12
/opt/homebrew/bin/python3.12 -m venv .venv
source .venv/bin/activate
pip install -U pip manim
```

### TeX (for `MathTex`)

This machine uses [TinyTeX](https://yihui.org/tinytex/) under `~/Library/TinyTeX` (no sudo). Put its bin dir on `PATH` before rendering:

```bash
export PATH="$PATH:$HOME/Library/TinyTeX/bin/universal-darwin"
```

Add that line to `~/.zshrc` (or `~/.bash_profile`) so new shells pick it up. Smoke check:

```bash
source .venv/bin/activate
manim -ql scenes/mathtex_smoke.py MathTexSmoke
```

`Text` still works without TeX for quick labels.

## Render a scene

```bash
source .venv/bin/activate
manim -ql scenes/hello.py HelloAxes
```

`-ql` is low quality (fast). Use `-qh` when you want a cleaner render. Output lands in `media/` (gitignored).

## Meanwhile

Work is tracked in Jira project `MAN` on macovin.atlassian.net. See `AGENTS.md`.
