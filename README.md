# Portable Agents

An open-source starter for a customer-owned agent package. A desktop host will work with local files and connected services while a paired phone starts and follows the same tasks by voice or text. An orchestrator delegates to specialists for files, email, presentations, and website maintenance.

Customers choose their AI operator independently of the agent's skills and approval rules. The intended ChatGPT path is OpenAI's [Sign in with ChatGPT for open-source clients](https://developers.openai.com/siwc/quickstart), subject to eligibility and granted scopes. Claude should use a supported Anthropic API credential or another officially permitted route; a Claude subscription alone is not assumed to be an app credential. OpenRouter and the OpenAI API can be optional adapters using customer-supplied credentials. ChatGPT sign-in does not grant access to the customer's ChatGPT conversations or files. See [provider contract](docs/provider-contract.md).

This repository is currently a design and manifest starter. Desktop hosting, mobile pairing, voice, provider connections, and specialist tools are not implemented. See [the architecture sketch](docs/architecture.md) for the proposed workflow, approval boundaries, and the website agent's separate paths for simple Git-backed sites and database-backed sites.

## Try the example

```bash
python3 scripts/validate_agents.py
python3 -m unittest discover -s tests
```

Each folder under `agents/` contains `agent.json` and `instructions.md`. Copy a folder to use its prompt and metadata in a compatible runner. No provider connection or API access is included yet.
