"""Structural validator for ICM workspaces — the agnostic "lint pass".

Checks a workspace against the rules in conventions.md / portability.md:
  - root AGENTS.md present (the only Layer-0 file with real content)
  - root CONTEXT.md present (Layer-1 task routing)
  - each harness shim present and redirecting to AGENTS.md
  - at least one stage exists
  - every stage has a CONTEXT.md with ## Inputs / ## Process / ## Outputs
    (matched as real H2 headings, not substrings)
  - stage numbering has no duplicates and is contiguous from 01

These checks, and only these, are what "validator-clean" guarantees. conventions.md
documents further line-level rules (Inputs tagging, Outputs format, harness
neutrality, slug style) that are conventions, not mechanically enforced here.

Stdlib only. Library use: `validate_workspace(path) -> list[Finding]`.
CLI: `python3 icm-core/validate.py <workspace>` — prints findings, exits 1 on error.
"""
import os
import re
import sys
from dataclasses import dataclass

# The default shim set (D5). AGENTS.md is canonical content, not a shim.
# Forward-slash literals: portable for open() on every platform and for messages.
DEFAULT_SHIMS = ["CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md"]
REQUIRED_SECTIONS = ["Inputs", "Process", "Outputs"]
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


def _has_section(text, name):
    """True if `text` contains a real H2 heading `## <name>` on its own line."""
    return re.search(rf"(?m)^##[ \t]+{re.escape(name)}[ \t]*$", text) is not None


def validate_workspace(path):
    """Return a list of Finding for the workspace rooted at `path`."""
    findings = []

    # Layer 0 / Layer 1 root files
    if not os.path.isfile(os.path.join(path, "AGENTS.md")):
        findings.append(Finding("error", "MISSING_AGENTS",
                                "root AGENTS.md is missing (Layer-0 identity file)"))
    if not os.path.isfile(os.path.join(path, "CONTEXT.md")):
        findings.append(Finding("error", "MISSING_ROUTING",
                                "root CONTEXT.md is missing (Layer-1 task routing)"))

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
            m = STAGE_RE.match(name)
            if not os.path.isdir(stage_path) or not m:
                continue
            numbers.append(int(m.group(1)))
            contract = _read(os.path.join(stage_path, "CONTEXT.md"))
            if contract is None:
                findings.append(Finding("error", "MISSING_CONTRACT",
                                        f"stage {name} has no CONTEXT.md"))
                continue
            for section in REQUIRED_SECTIONS:
                if not _has_section(contract, section):
                    findings.append(Finding("error", "MISSING_SECTION",
                                            f"stage {name} contract missing section ## {section}"))

    # At least one stage
    if not numbers:
        findings.append(Finding("error", "NO_STAGES",
                                "workspace has no stages (expected stages/NN_<slug>/)"))
        return findings

    # Duplicate stage numbers
    dups = sorted({n for n in numbers if numbers.count(n) > 1})
    if dups:
        findings.append(Finding("error", "DUPLICATE_STAGE",
                                f"duplicate stage number(s): {['%02d' % n for n in dups]}"))

    # Contiguous numbering from 01 (over the distinct numbers)
    unique = sorted(set(numbers))
    expected = list(range(1, len(unique) + 1))
    if unique != expected:
        missing = sorted(set(expected) - set(unique))
        findings.append(Finding("error", "NONCONTIGUOUS",
                                f"stage numbering not contiguous from 01: "
                                f"found {['%02d' % n for n in unique]}, "
                                f"missing {['%02d' % n for n in missing]}"))

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
