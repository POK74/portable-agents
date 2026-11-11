# Repository Guidelines

## Project Structure & Module Organization

This repository hosts portable agent definitions. Keep each agent in `agents/<slug>/` with an `agent.json` manifest and an `instructions.md` prompt. Put provider adapters in `src/portable_agents/` when runtime code is added; keep provider-neutral behavior in the agent files. Use `examples/` for sample configuration and `tests/` for checks. Never commit credentials, chat exports, or local session files.

## Build, Test, and Development Commands

Run `python3 scripts/validate_agents.py` before committing; it checks every manifest and its referenced instructions file. Run `python3 -m unittest discover -s tests` for the validation tests. There is no compiled build or package release yet. To try an agent, copy its folder and supply credentials through your local environment or the selected provider's supported authentication flow.

## Coding Style & Naming Conventions

Use two-space indentation in JSON and four spaces in Python. Name agent directories with lowercase letters and hyphens, such as `research-helper`. Match the manifest `id` to its directory name. Write prompts in plain Markdown with a clear role, inputs, outputs, and limits. Keep provider-specific model names and endpoints in configuration, not in shared instructions.

## Testing Guidelines

Add a test under `tests/test_*.py` when changing manifest validation or runtime behavior. Include a failing example for each new validation rule. Run both commands above before opening a pull request. Do not require a live provider account for the default test suite.

## Commit & Pull Request Guidelines

The repository starts without an established commit convention. Use short imperative subjects such as `Add research helper agent` or `Validate instruction paths`. In pull requests, explain the agent's purpose or behavior change, show a sample invocation or output, and note which provider flows you checked. Link related issues when present.

## Security & Provider Configuration

Store API keys in environment variables and document required names in `examples/`; never place them in manifests. OpenRouter and OpenAI API integrations need their own supported credentials. A ChatGPT subscription must not be treated as an API credential; add any ChatGPT connection only through an officially supported flow.
