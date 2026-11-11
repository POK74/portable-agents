# Repository Guidelines

## Project Structure & Module Organization

This repository is the starter for a desktop host, paired mobile client, and specialist agents. Keep each agent in `agents/<slug>/` with an `agent.json` manifest and an `instructions.md` prompt. Put host, pairing, and provider adapters in `src/portable_agents/` when runtime code is added; keep provider-neutral behavior in agent files. Use `docs/` for architecture, `examples/` for configuration, and `tests/` for checks.

## Build, Test, and Development Commands

Run `python3 scripts/validate_agents.py` before committing; it checks every manifest and its referenced instructions file. Run `python3 -m unittest discover -s tests` for validation tests. There is no desktop or mobile build yet. Follow `docs/architecture.md` when adding runtime components.

## Coding Style & Naming Conventions

Use two-space indentation in JSON and four spaces in Python. Name agent directories with lowercase letters and hyphens, such as `research-helper`. Match the manifest `id` to its directory name. Write prompts in plain Markdown with a clear role, inputs, outputs, and limits. Keep provider-specific model names and endpoints in configuration, not in shared instructions.

## Testing Guidelines

Add a test under `tests/test_*.py` when changing manifest validation or runtime behavior. Include a failing example for each new validation rule. Run both commands above before opening a pull request. Do not require a live provider account for the default test suite.

## Commit & Pull Request Guidelines

The repository starts without an established commit convention. Use short imperative subjects such as `Add research helper agent` or `Validate instruction paths`. In pull requests, explain the agent's purpose or behavior change, show a sample invocation or output, and note which provider flows you checked. Link related issues when present.

## Security & Provider Configuration

Keep API keys and OAuth tokens out of manifests and Git. Keep the agent workflow independent of the selected AI operator; follow `docs/provider-contract.md`. For an open-source ChatGPT connection, use OpenAI's official sign-in flow and verify granted scopes. For Claude, use an officially supported Anthropic integration. Do not ask for session cookies. Keep API keys in local secure storage. Require customer approval before sending email or attachments, publishing site changes, or spending money. Restrict file access to customer-selected folders, and make paired phones revocable.
