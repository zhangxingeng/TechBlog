---
date: 2024-09-17
title: "LLM Metrics"
---
### Relevancy
- A is relevant to C
- Use llm to determine wether an answer is relevant or not
- disadv: depend on a good language model, complex things limits the accuracy of this value
- Example prompt: 
    ```python
    '''
    Context: {context}
    Answer: {answer}
    Evaluate the relevance of the answer to the given question. Consider the following:
    1. Does the answer directly address the question?
    2. Is all the information in the answer related to the question?
    3. Does the answer provide any irrelevant or off-topic information?
    '''
    ```

### Faithfulness
- A is supported by C
- Identify hallucinations, ensure answer is grounded
- Example prompt: 
    ```python
    '''
    Question: {question}
    Context: {context}
    Answer: {answer}
    Evaluate how well the answer captures the relevant information from the context. Consider the following:
    1. What key points from the context are relevant to the question?
    2. How many of these relevant points are included in the answer?
    3. Is there any important information from the context missing in the answer?
    '''
    ```

### Context Recall
- Example prompt: 
    ```python
    '''
    Question: {question}
    Context: {context}
    Answer: {answer}

    Evaluate how well the answer captures the relevant information from the context. Consider the following:
    1. What key points from the context are relevant to the question?
    2. How many of these relevant points are included in the answer?
    3. Is there any important information from the context missing in the answer?
    '''
    ```