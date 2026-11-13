# Writes one joke about AI coding agents to /output/entry.txt.
import os

JOKE = "My coding agent has told me \"You're absolutely right!\" 212 times today. The one time it disagreed, I was."

out = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
