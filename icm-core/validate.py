"""Structural validator for ICM workspaces — the agnostic "lint pass".

Checks a workspace against the conventions in conventions.md / portability.md:
  - root AGENTS.md present (the only Layer-0 file with real content)
  - each harness shim present and pointing at AGENTS.md
  - every stage has a CONTEXT.md with ## Inputs / ## Process / ## Outputs
  - stage numbering is contiguous from 01

Stdlib only. Library use: `validate_workspace(path) -> list[Finding]`.
CLI: `python3 icm-core/validate.py <workspace>` — prints findings, exits 1 on error.
"""
import os
import re
import sys
from dataclasses import dataclass

# The default shim set (D5). AGENTS.md is canonical content, not a shim.
DEFAULT_SHIMS = ["CLAUDE.md", "GEMINI.md", os.path.join(".github", "copilot-instructions.md")]
REQUIRED_SECTIONS = ["## Inputs", "## Process", "## Outputs"]
STAGE_RE = re.compile(r"^(\d{2})_")


@dataclass
class Finding:
    level: str   # "error" | "warn"
    code: str
    message: str

    def __str__(self):
        return f"{self.level} {self.code}: {self.message}"


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError):
        return None


def validate_workspace(path):
    """Return a list of Finding for the workspace rooted at `path`."""
    findings = []

    # Layer 0: AGENTS.md
    if not os.path.isfile(os.path.join(path, "AGENTS.md")):
        findings.append(Finding("error", "MISSING_AGENTS",
                                "root AGENTS.md is missing (Layer-0 identity file)"))

    # Harness shims — present and redirecting to AGENTS.md
    for shim in DEFAULT_SHIMS:
        text = _read(os.path.join(path, shim))
        if text is None:
            findings.append(Finding("error", "MISSING_SHIM",
                                    f"harness shim {shim} is missing"))
        elif "AGENTS.md" not in text:
            findings.append(Finding("error", "BAD_SHIM",
                                    f"shim {shim} does not redirect to AGENTS.md"))

    # Stages
    stages_dir = os.path.join(path, "stages")
    numbers = []
    if os.path.isdir(stages_dir):
        for name in sorted(os.listdir(stages_dir)):
            stage_path = os.path.join(stages_dir, name)
            if not os.path.isdir(stage_path):
                continue
            m = STAGE_RE.match(name)
            if not m:
                continue
            numbers.append(int(m.group(1)))
            contract = _read(os.path.join(stage_path, "CONTEXT.md"))
            if contract is None:
                findings.append(Finding("error", "MISSING_CONTRACT",
                                        f"stage {name} has no CONTEXT.md"))
                continue
            for section in REQUIRED_SECTIONS:
                if section not in contract:
                    findings.append(Finding("error", "MISSING_SECTION",
                                            f"stage {name} contract missing section {section}"))

    # Contiguous numbering from 01
    if numbers:
        expected = list(range(1, len(numbers) + 1))
        if sorted(numbers) != expected:
            findings.append(Finding("error", "NONCONTIGUOUS",
                                    f"stage numbering not contiguous from 01: found {sorted(numbers)}"))

    return findings


def main(argv):
    if len(argv) != 2:
        print("usage: python3 validate.py <workspace-path>", file=sys.stderr)
        return 2
    findings = validate_workspace(argv[1])
    for f in findings:
        print(f)
    return 1 if any(f.level == "error" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
