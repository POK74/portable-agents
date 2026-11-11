# AI operator contract

The agent package owns task planning, tool permissions, customer approvals, and audit records. The selected AI operator supplies model responses only. Each adapter should expose capability discovery, a request method, cancellation, and clear errors for authentication, limits, and unsupported features.

| Operator | Intended connection | Current state |
| --- | --- | --- |
| ChatGPT plan | Official Sign in with ChatGPT for eligible open-source clients | Planned |
| OpenAI API | Customer API project key | Planned |
| Claude | Anthropic Console API key or another officially supported integration | Planned |
| OpenRouter | Customer API key | Planned |

Never reuse a ChatGPT or Claude website session cookie as an integration credential. Do not silently fall back to another provider when the chosen operator fails. Show the operator, model, and expected billing path in setup. The customer can change operators without migrating agent definitions or granting new access to local files, mail, GitHub, or Vercel.

For the Storo pilot, the website workflow should work with a fake adapter in tests before any live AI provider is connected: request → proposed file change → validation → preview → customer approval → publication. The AI response is untrusted input; validate the proposed files and keep deployment permissions in the application, not in the model prompt.
