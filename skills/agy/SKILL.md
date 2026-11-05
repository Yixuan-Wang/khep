---
name: agy
description: Use Google Gemini models through the Antigravity CLI (agy).
---

# Google Gemini via Antigravity CLI

Use the following Antigravity CLI (`agy`) command to invoke Google Gemini models non-interactively.

```sh
agy -p "$PROMPT" --model $MODEL --effort $EFFORT --settings '{"permissions":{"allow":["read_file(*)","read_url(*)"]}}'
```

## Instructions

- Available effort levels are `low`, `medium`, and `high`.
- Use `@` syntax to mention files and directories; line range syntax is also supported.
- For writing files, interacting with websites, running commands, and using MCP, check [permissions.md](references/permissions.md).
  An empty response may indicate permission denial.
- For multi-turn usage, `--output-format` needs to be `json`. See [multi-turn.md](references/multi-turn.md).

Additional useful commands:

```sh
# List available Gemini models
agy models 2>/dev/null | rg '(gemini-.*)-low' -or '$1'

# Pipe a prompt
echo "$PROMPT" | agy -p "$(</dev/stdin)" --model $MODEL --effort $EFFORT

# Using JSON output, timeout, and stderr redirect
agy -p "$PROMPT" \
  --model $MODEL --effort $EFFORT \
  --output-format json \
  --print-timeout 10m \
  --settings '{"permissions":{"allow":["read_file(*)","read_url(*)"]}}' \
  2>/tmp/agy.txt | jq -r 'if .status=="SUCCESS" then .response else ("ERROR: "+(.error//"unknown")) end'

# Using structured output
agy -p "Parse the semantic version string v2.14.3 into an object with integer fields major, minor, and patch." \
  --model $MODEL --effort $EFFORT \
  --output-format json \
  --json-schema '{"type":"object","properties":{"major":{"type":"integer"},"minor":{"type":"integer"},"patch":{"type":"integer"}},"required":["major","minor","patch"]}' \
  | jq '.structured_output'
```

## References

- [Headless mode](https://antigravity.google/docs/cli/headless.md)
- [Settings](https://antigravity.google/docs/settings.md)
- [CLI Reference](https://antigravity.google/docs/cli/reference.md)
