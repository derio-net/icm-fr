"""Structural-validator tests for ICM workspaces (TDD — written before validate.py).

Stdlib unittest only, no third-party deps, so this runs on any harness.
Run from repo root:  python3 icm-core/test_validate.py
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate import validate_workspace, DEFAULT_SHIMS  # noqa: E402


CONTRACT = "## Inputs\n- x (reference)\n\n## Process\n1. do\n\n## Outputs\n- y -> output/\n"


def _write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(text)


def _build_workspace(root, *, agents=True, routing=True, shims=None, stages=None):
    """Construct a workspace on disk. stages: list of (dirname, contract_text)."""
    if agents:
        _write(os.path.join(root, "AGENTS.md"), "# Workspace\nLayer 0 identity.\n")
    if routing:
        _write(os.path.join(root, "CONTEXT.md"), "# Routing\nLayer 1.\n")
    for shim in (DEFAULT_SHIMS if shims is None else shims):
        _write(os.path.join(root, shim), "This workspace uses AGENTS.md. Read ./AGENTS.md.\n")
    if stages is None:
        stages = [("01_outline", CONTRACT), ("02_draft", CONTRACT)]
    for name, contract in stages:
        _write(os.path.join(root, "stages", name, "CONTEXT.md"), contract)


def _errors(findings):
    return [f for f in findings if f.level == "error"]


class ValidateWorkspaceTest(unittest.TestCase):
    def test_valid_workspace_has_no_errors(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root)
            self.assertEqual(_errors(validate_workspace(root)), [])

    def test_missing_agents_md(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root, agents=False)
            errs = _errors(validate_workspace(root))
            self.assertTrue(any("AGENTS.md" in e.message for e in errs))

    def test_missing_routing_context(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root, routing=False)
            codes = {e.code for e in _errors(validate_workspace(root))}
            self.assertIn("MISSING_ROUTING", codes)

    def test_missing_shim(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root, shims=["CLAUDE.md", ".github/copilot-instructions.md"])
            errs = _errors(validate_workspace(root))
            self.assertTrue(any("GEMINI.md" in e.message for e in errs))

    def test_bad_shim_does_not_reference_agents(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root)
            _write(os.path.join(root, "CLAUDE.md"), "do whatever you like\n")
            errs = _errors(validate_workspace(root))
            self.assertTrue(any("CLAUDE.md" in e.message for e in errs))

    def test_missing_contract_section(self):
        with tempfile.TemporaryDirectory() as root:
            no_outputs = "## Inputs\n- x (reference)\n\n## Process\n1. do\n"
            _build_workspace(root, stages=[("01_outline", CONTRACT), ("02_draft", no_outputs)])
            errs = _errors(validate_workspace(root))
            self.assertTrue(any("02_draft" in e.message and "Outputs" in e.message for e in errs))

    def test_section_heading_must_be_real_h2_not_substring(self):
        with tempfile.TemporaryDirectory() as root:
            # H3 and a suffixed heading must NOT satisfy the required H2 sections.
            sneaky = "### Inputs\n- x\n\n## Processing\n1. do\n\n## Outputs\n- y -> output/\n"
            _build_workspace(root, stages=[("01_only", sneaky)])
            errs = _errors(validate_workspace(root))
            missing = {e.message for e in errs if e.code == "MISSING_SECTION"}
            self.assertTrue(any("Inputs" in m for m in missing))   # ### Inputs rejected
            self.assertTrue(any("Process" in m for m in missing))  # ## Processing rejected

    def test_no_stages_is_an_error(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root, stages=[])
            codes = {e.code for e in _errors(validate_workspace(root))}
            self.assertIn("NO_STAGES", codes)

    def test_duplicate_stage_number_reported_as_duplicate(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root, stages=[("01_a", CONTRACT), ("01_b", CONTRACT)])
            errs = _errors(validate_workspace(root))
            codes = {e.code for e in errs}
            self.assertIn("DUPLICATE_STAGE", codes)
            # A pure duplicate must NOT be mislabeled as a numbering gap.
            self.assertNotIn("NONCONTIGUOUS", codes)

    def test_noncontiguous_numbering_names_the_gap(self):
        with tempfile.TemporaryDirectory() as root:
            _build_workspace(root, stages=[("01_outline", CONTRACT), ("03_draft", CONTRACT)])
            errs = [e for e in _errors(validate_workspace(root)) if e.code == "NONCONTIGUOUS"]
            self.assertTrue(errs)
            self.assertIn("02", errs[0].message)  # message names the missing number


if __name__ == "__main__":
    unittest.main(verbosity=2)
