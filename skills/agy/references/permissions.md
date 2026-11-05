Use the `--settings '{"permissions":{<...>}}'` CLI flag to control action permissions (`allow` or `deny`). Actions available for control:

| Action | Target Format |
| :--- | :--- |
| `read_file` | `read_file(/path)`, `read_file(dir)`, or `read_file(*)` |
| `write_file` | `write_file(/path)` or `write_file(*)` |
| `read_url` | `read_url(domain)` or `read_url(*)` |
| `execute_url` | `execute_url(domain)` or `execute_url(*)` |
| `command` | `command(prefix)`, `command(regex:pattern)`, or `command(*)` |
| `mcp` | `mcp(server/tool)`, `mcp(server/*)`, or `mcp(*)` |

- Web search is always allowed to prevent hallucination.
- The `--dangerously-skip-permissions` flag bypasses all permission checks. Deny rules override it.
- Denied actions are printed to stderr and recorded at `.denied_actions` in JSON responses.
