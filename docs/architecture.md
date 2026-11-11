# Architecture sketch

```mermaid
flowchart LR
    M[Mobile voice and text] <-->|Authenticated task channel| R[Pairing and relay]
    R <-->|Encrypted connection| P[Desktop host on customer PC]
    P --> O[Orchestrator]
    O --> F[Files]
    O --> E[Email]
    O --> S[Presentations]
    O --> W[Website]
    O --> AI[Chosen AI provider]
```

The desktop host owns local file permissions, task state, and provider connections. The phone submits requests and shows progress. Pair each phone explicitly and allow revocation. When the PC is offline, tasks that need its files wait.

The orchestrator breaks a request into steps and gives each specialist only the access needed for its step. The files agent searches customer-approved folders. The email agent drafts and sends through an authorized mail connection. The presentation agent creates and revises slides. The website agent prepares fixes in a reviewable workspace and shows a preview or diff before deployment.

For a request from the car to email a PC file: transcribe the request, find candidate files, resolve ambiguity, prepare the draft, confirm the recipient and exact attachment by voice or on screen, then send and return a receipt. Sending email or files, publishing a live website, and spending money require explicit customer approval. Keep credentials in local secure storage and an audit record of approvals without recording sensitive file contents by default.

Build order: desktop host and task state; orchestrator; mobile pairing and task channel; files and email draft flow; voice input; presentations and website specialists. Add official ChatGPT sign-in and optional provider adapters behind a shared model interface.
