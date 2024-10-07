---
title: "Langchain different Prompt Templates and When to Use Them"
date: 2024-10-05
---

### Categories
```text
BasePromptTemplate --*Abstract class not used directly*
├── PipelinePromptTemplate --*Allow prompt chaining and output to input workflow*
├── StringPromptTemplate --*abstract class, allow string inputs*
│   ├── PromptTemplate --*Basic prompt allow variable injection*
│   ├── FewShotPromptTemplate --*Allow for `list(Example())` inputs as few shot training* 
│   └── FewShotPromptWithTemplates --*more complex than prev, used when examples need intricate formatting*
├── BaseChatPromptTemplate --*chat based prompts for conversations*
│   ├── AutoGPTPrompt --*for autonomous agents to execute tasks*
│   └── ChatPromptTemplate  --*for chat-based interactions manages flow of dialogue between participants(user, assistant)*
│       └── AgentScratchPadChatPromptTemplate --*Give Agent a "Scratchpad to write down intermediate thoughts before final answer*
└── BaseMessagePromptTemplate --*  *
    ├── MessagesPlaceholder
    └── BaseStringMessagePromptTemplate 
        ├── ChatMessagePromptTemplate
        ├── HumanMessagePromptTemplate
        ├── AIMessagePromptTemplate
        └── SystemMessagePromptTemplate
```
