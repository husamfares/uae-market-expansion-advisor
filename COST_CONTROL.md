# API Usage and Cost Control

API usage was managed carefully due to the limited OpenAI budget provided for the assignment.

Several strategies were used:

- The planner routes each question only to the necessary specialist agents instead of calling all agents.
- Prompts were designed to be concise and structured to reduce token usage.
- A deterministic validator was used instead of an LLM validator to avoid additional API calls.
- The system uses a lightweight JSON knowledge layer rather than a full RAG pipeline.

These design decisions help keep the system efficient while still producing useful responses.
