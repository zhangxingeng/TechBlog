---
date: 2025-06-01
title: "Notes on ML System Design Interview"
---

- Ask detailed questions to grasp what the interviewer expects
- request a 1-2 minute to organize thoughts and draft a solution
- Proactively explain your thoughts and considerations instead of waiting for the interviewer to ask
- Regularly pause and ask the interviewer if they have any questions
- Discuss trade-offs and justify your decisions

### Different Things to Think of When Designing ML Systems
- **Problem Scope**: What are the required features? Does the prediction need to be personalized?
- **Data**: data scale? labeled? Available data resources? structured or unstructured? File format? modalities single or multimodal?
- **Resource Constraints**: Budget for time? Human resources? Money (compute, labeler)? Hardware/memory limit? Will the system on the cloud or on-prem?
- **Execution Constraints**: Latency? Throughput (time to complete response, Time-to-first-token, Time-between-token, Tokens-per-second)
- **Business Goals**: reduce live support calls? build user relationship?

### Picking tools
- Agent (LLM): 
  - Prompt: is chain-of-thought required? (check resources 1 and 2 for details)
  - Model: Which model? Model size? Context Length? hardware requirements? text only or multimodal? (use chatbot arena: (#3 in resources below))
  - pre-training? fine-tuning (good at one task) / Alignment (Making sure the AI behave according to human values)? 
    - RLHF (reinforcement learning from human feedback): used where human preferences are valued (ethics and safety)
    - DPO (Direct Preference OptimizationF): use an explicit collection of data to guide the optimization process
    - Chain-of-hindsight: learning from past mistakes by re-evaluating decision with the benefit of hindsight (like chess playing)
    - ORPO (Optimizing by Rules and Preferences): Ensure the model adheres to certain rules (used when strict adherence to rules is required)

    #### Relevant Resources
    1. [How to engineer good prompt](https://github.com/dair-ai/Prompt-Engineering-Guide)
    2. [Modern Advances in Prompt Engineering](https://cameronrwolfe.substack.com/p/modern-advances-in-prompt-engineering)
    3. [Chatbot Arena](https://chat.lmsys.org/?leaderboard=)

### Vector Store
- Data preprocessing:
  - How to convert raw data to embedding ready data?
  - Chunk size, overlapping chunk size, splitting techniques?
  - How to handle non-plain text data?
  - How to extract metadata?
- Embeddings: Sparse, dense, multi-vector, long-context dense, variable-dimension, code embedding? multi-modal?
- Indexing/retriveval: 
- Unfinished: https://towardsdatascience.com/mastering-genai-ml-system-design-interview-principles-solution-outline-71a4664511a7