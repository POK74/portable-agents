# Portable Agents

An open-source starter for a customer-owned agent package. A desktop host will work with local files and connected services while a paired phone starts and follows the same tasks by voice or text. An orchestrator delegates to specialists for files, email, presentations, and website maintenance.

The intended ChatGPT path is OpenAI's [Sign in with ChatGPT for open-source clients](https://developers.openai.com/siwc/quickstart), subject to eligibility and granted scopes. OpenRouter and the OpenAI API can be optional adapters using customer-supplied credentials. ChatGPT sign-in does not grant access to the customer's ChatGPT conversations or files.

This repository is currently a design and manifest starter. Desktop hosting, mobile pairing, voice, provider connections, and specialist tools are not implemented. See [the architecture sketch](docs/architecture.md) for the proposed workflow and approval boundaries.

## Try the example

```bash
python3 scripts/validate_agents.py
python3 -m unittest discover -s tests
```

Each folder under `agents/` contains `agent.json` and `instructions.md`. Copy a folder to use its prompt and metadata in a compatible runner. No provider connection or API access is included yet.
