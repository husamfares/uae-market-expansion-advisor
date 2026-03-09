# Architecture Overview

The system follows a lightweight agentic architecture built using the Agno framework. The user interacts with the system through a CLI interface. The request is then processed by an orchestrator that coordinates the entire workflow.

## System Flow

User → CLI Interface → Orchestrator → Planner → Specialist Agents → Knowledge Tools → Orchestrator Synthesizer → Deterministic Validator → Final Executive Recommendation.

The planner analyzes the user question and decides which specialist agents should be involved in generating the answer.

Each specialist agent focuses on a specific domain such as:

- Location strategy
- Competitor analysis
- Menu design
- Pricing strategy
- Marketing strategy
- Operations planning
- Market entry considerations
- Licensing considerations

The specialist agents can call knowledge tools that retrieve structured insights from the project’s knowledge layer. The knowledge layer contains UAE restaurant market context and Abu Dhabi tourism restaurant license data.

After collecting responses from the selected agents, the Orchestrator Synthesizer combines their outputs into a single structured recommendation designed for executive decision-making.

Finally, a deterministic validator checks the final answer to ensure that the response is complete, structured, and not empty before returning the final result to the user.

## Architecture Diagram

![Architecture Diagram](architecture_diagram.png)
