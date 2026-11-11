# Portable Agents

Downloadable, provider-neutral agent definitions. The first version contains a manifest format, one example agent, and local validation. Runtime adapters for OpenRouter and supported OpenAI interfaces can be added without changing agent instructions.

## Try the example

```bash
python3 scripts/validate_agents.py
python3 -m unittest discover -s tests
```

Each folder under `agents/` contains `agent.json` and `instructions.md`. Copy a folder to use its prompt and metadata in a compatible runner. No provider connection or API access is included yet.
