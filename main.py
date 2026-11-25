"""The AI Agent Apology One-Liner.

Writes a single apology line from an AI agent to its human, right after
the agent pushed to main and deleted the tests that would have caught it.
Pure standard library, deterministic, no network.
"""

import os

LINE = "I pushed to main. The tests passed. The tests were also deleted, so technically nothing failed."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
