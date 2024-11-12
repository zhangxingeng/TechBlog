---
title: "Notes on Graph RAG"
date: 2024-11-12
---


## [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/pdf/2404.16130)

### What is "Sensemaking"?
"“a motivated, continuous effort to understand connections in order to anticipate their trajectories and act effectively” (Klein et al., 2006a)

### Procedure
1. Source Documents -> Text Chunks
    - chunk size of 600 token can extract 2x than 2400 token
    - balance precision and recall
2. Text Chunks -> Element Instances
    - First Use multipart LLM prompt to identify *entities* in the text (e.g. name, type, description)
    - Then identify all *relationships* between clearly-related entities. 
# TODO: page 4