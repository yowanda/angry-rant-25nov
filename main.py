"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about a small everyday annoyance to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (``/output`` when the variable is unset).

Deterministic: the same fixed text on every run. Standard library only,
no network access, writes only inside the output directory.
"""

import os

RANT = (
    "The self-checkout just accused me of stealing my own shopping. "
    "'Unexpected item in the bagging area.' Unexpected? I put it there. "
    "You watched me. Now a light is flashing, a queue is staring, and a "
    "teenager has to come over and type a code like I'm on parole for "
    "buying oat milk. I scanned it. I bagged it. I paid for it. The only "
    "thing unexpected here is that this machine still has a job."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(RANT)


if __name__ == "__main__":
    main()
