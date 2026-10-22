#!/usr/bin/env bash
# Thin wrapper — delegates to the plan validator of the installed super-fr,
# on any harness: the `fr` CLI's bundled copy first, then the Claude Code
# marketplace copy for an `fr` too old to carry one.
if command -v fr >/dev/null 2>&1 && fr validate plans --help >/dev/null 2>&1; then
  exec fr validate plans "$@"
fi
legacy="$HOME/.claude/plugins/marketplaces/derio-net--super-fr/scripts/validate-plans.sh"
if [ -x "$legacy" ]; then
  exec "$legacy" "$@"
fi
echo 'validate-plans: no super-fr plan validator found; install/upgrade fr' >&2
exit 127
