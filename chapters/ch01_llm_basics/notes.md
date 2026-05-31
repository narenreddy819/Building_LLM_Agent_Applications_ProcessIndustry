\# Chapter 1 - LLMs \& Agentic AI



\## Purpose of this Chapter



Understand the building blocks of Agentic AI systems before writing code.



The goal is not to learn theory in depth but to understand how modern AI applications are built.



\---



\## What is an LLM?



LLM (Large Language Model) is a neural network trained to predict the next token in a sequence.



Example:



Input:



The capital of India is



Output:



New Delhi



By repeatedly predicting the next token, LLMs can generate explanations, summaries, code, and conversations.



Examples of LLMs:



\* GPT

\* Claude

\* Gemini

\* Qwen

\* DeepSeek

\* Llama



Key Insight:



LLMs are not databases.

LLMs are pattern prediction engines.



\---



\## Why are LLMs Useful?



Because they are trained on:



\* Books

\* Websites

\* Documentation

\* Research papers

\* Source code



This allows them to:



\* Answer questions

\* Summarize content

\* Generate code

\* Assist users through natural language



\---



\## LLM vs Traditional Machine Learning



Traditional ML:



Input Data

→ Model

→ Prediction



Example:



Compressor vibration

→ Failure prediction



LLM:



Text Input

→ Reasoning

→ Text Output



Example:



Why is compressor discharge pressure dropping?



→ Natural language explanation



\---



\## What is an AI Agent?



An AI Agent is an LLM that can take actions.



Agent = LLM + Tools



Examples of actions:



\* Query database

\* Read documents

\* Execute Python code

\* Call APIs

\* Search knowledge base



Without tools, an LLM can only generate text.



With tools, it can perform useful work.



\---



\## Core Components of an Agent



Agent =



\* LLM (Brain)

\* Tools (Actions)

\* Memory

\* Context

\* Instructions



These components determine agent quality.



\---



\## Context Engineering



Most important concept in this chapter.



Prompt Engineering focuses on:



"What question should I ask?"



Context Engineering focuses on:



"What information should the model see?"



Examples:



\* SOPs

\* Equipment manuals

\* Historian data

\* Maintenance logs

\* Previous conversations



Better context generally produces better answers.



\---



\## Hallucination



LLMs can generate convincing but incorrect answers.



This is called hallucination.



Industrial systems must minimize hallucinations because incorrect answers can lead to operational risks.



Methods to reduce hallucinations:



\* RAG

\* Better context

\* Tool usage

\* Grounding with plant documentation



\---



\## Retrieval Augmented Generation (RAG)



RAG =



Retrieve

\+

Augment Context

\+

Generate



Workflow:



User Question

→ Search Documents

→ Retrieve Relevant Content

→ Inject into Context

→ Generate Response



Benefits:



\* More accurate answers

\* Uses plant-specific knowledge

\* Reduces hallucination



\---



\## Multi-Agent Systems



Instead of one large agent, create specialized agents.



Example:



Orchestrator Agent



\* Historian Agent

\* Documentation Agent

\* Analytics Agent

\* Reporting Agent



Advantages:



\* Better specialization

\* Cleaner architecture

\* Easier maintenance



\---



\## Industrial Use Cases



1\. Operator Assistant



&#x20;  \* Query SOPs

&#x20;  \* Query manuals

&#x20;  \* Troubleshooting support



2\. Historian Analytics Assistant



&#x20;  \* Analyze process trends

&#x20;  \* Explain anomalies



3\. Maintenance Assistant



&#x20;  \* Search work orders

&#x20;  \* Suggest diagnostics



4\. Safety Assistant



&#x20;  \* Retrieve procedures

&#x20;  \* Check compliance requirements



\---



\## Key Takeaways



1\. LLM = Reasoning Engine

2\. Agent = LLM + Tools

3\. Context Engineering is critical

4\. RAG provides domain knowledge

5\. Multi-Agent systems scale better than one large agent

6\. Industrial AI applications require grounding and reliability



