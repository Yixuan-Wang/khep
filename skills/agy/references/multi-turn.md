Use the resuming mechanism to follow up on a previous conversation:

```sh
# Turn 1: start, print the response, and capture the ID
OUT=$(agy -p "Remember the secret word: pineapple. Reply OK." \
  --model $MODEL --effort $EFFORT --output-format json 2>/dev/null)
ID=$(jq -r .conversation_id <<<"$OUT")
jq -r .response <<<"$OUT"

# Turn 2+: resume with the ID
agy -p "What was the secret word?" --conversation "$ID" \
  --model $MODEL --effort $EFFORT --output-format json 2>/dev/null \
  | jq -r .response
```

- You can resume a conversation from any directory.
- Pass `--model` and `--effort` on every turn.
- An unknown ID silently starts a new conversation.
