# Key Design Decisions

Several design decisions were made to improve the quality and structure of the advisory system.

## Planner Agent

The planner agent interprets the user’s question and decides which specialist agents should respond. Without the planner, the system would rely on simple keyword matching, which would limit the system to very explicit queries. The planner allows the system to handle broader and more natural executive questions.

## Knowledge Layer

A structured knowledge layer was created using JSON data sources. This layer includes UAE restaurant market insights and Abu Dhabi tourism restaurant license data. Without this layer, the system would produce generic answers based only on the language model. The knowledge layer improves grounding and makes the recommendations more realistic.

## Prompting Strategy

A structured prompting style was used across all specialist agents. The prompts encourage deeper reasoning and structured executive-level responses. This prompting style helps produce clearer and more actionable answers.

## Orchestrator

The orchestrator acts as the controller of the entire system. It manages the workflow between the planner, the specialist agents, the knowledge tools, and the validator.

## Orchestrator Synthesizer

The synthesizer combines outputs from multiple specialist agents into one clear and structured executive recommendation.

## Deterministic Validator

The validator acts as a final quality gate before returning the answer to the user. It checks that the output is not empty, not too short, and follows the expected structure.
