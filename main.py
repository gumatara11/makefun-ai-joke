"""ai-joke-03 entry: writes one original one-liner about AI coding agents
to /output/entry.txt. Deterministic, standard library only, no network.
The gate takes UTF-8 text of 1 to 280 characters, so the joke is
validated here before it is written."""

import os

JOKE = "I gave my coding agent one ticket. It closed it, opened twelve more, assigned them all to me, and marked itself 'blocked by human.'"

assert 1 <= len(JOKE) <= 280 and any(not c.isspace() for c in JOKE)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
