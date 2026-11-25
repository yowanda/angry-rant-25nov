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


def _validate(text: str) -> bytes:
    """Validate the rant and return its exact UTF-8 bytes.

    Gate rules: 1-400 characters, not whitespace-only, must encode as
    UTF-8. The bytes are produced here so writing is deterministic and
    byte-exact on every run.
    """
    if not isinstance(text, str) or not 1 <= len(text) <= 400:
        raise ValueError(f"rant must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("rant must not be whitespace-only")
    return text.encode("utf-8")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = _validate(RANT)
    with open(path, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
