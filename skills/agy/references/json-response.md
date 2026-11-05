

| Field | Type | Description |
| --- | --- | --- |
| `conversation_id` | string | ID of the conversation, for resuming later |
| `status` | string | Terminal status (refer to [Status values](#status-values)) |
| `response` | string | The agent’s free-text response |
| `error` | string | Error message; present only on failure |
| `duration_seconds` | number | Wall-clock duration of the run |
| `num_turns` | number | Number of user turns in the conversation |
| `structured_output` | object | Parsed schema output; present only with `--json-schema` |
| `json_schema` | object | The schema that was enforced; present only with `--json-schema` |
| `usage` | object | Token counts: `input_tokens`, `output_tokens`, `thinking_tokens`, `cache_read_tokens`, `total_tokens` |
