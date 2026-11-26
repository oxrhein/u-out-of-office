"""The funniest out-of-office reply - make.fun entry.

Writes a single-line out-of-office auto-reply to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

def get_line():
    # One line, 131 characters. The gate (RULES.txt) allows 1-140.
    return "I'm away until Monday. My inbox is guarded by a houseplant. It can't read, can't reply, and — unlike me — has excellent boundaries."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(get_line())

if __name__ == "__main__":
    main()
