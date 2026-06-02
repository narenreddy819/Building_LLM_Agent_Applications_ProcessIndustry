# Chapter 4 - LLMs Under the Hood (Fast Revision)

## Big Picture

LLMs do not understand words directly.

They convert text into numbers, process those numbers through many layers, and predict the next token.

---

## Complete LLM Pipeline

Text
↓
Tokenization
↓
Token IDs
↓
Embeddings
↓
Attention
↓
Transformer Layers
↓
Language Model Head
↓
Next Token Prediction
↓
Response

---

## 1. Tokenization

Purpose:
Break text into smaller units called tokens.

Examples:

compressor
↓
compress + or

instrumentation
↓
instrument + ation

Key Learning:

LLMs work with tokens, not words.

Tokens determine:

* Cost
* Context Window Usage
* Processing Time

---

## 2. Token IDs

Each token gets a unique ID.

Example:

compress → 1256
or → 45

Text becomes:

[1256, 45]

Key Learning:

Token IDs contain no meaning.
They are only indexes.

---

## 3. Embeddings

Purpose:
Convert token IDs into vectors (lists of numbers).

Example:

Token ID 45
↓
Embedding Matrix Lookup
↓
Vector

Important:

Token ID 45 does not generate a vector.

Instead:

EmbeddingMatrix[45]
↓
Returns stored vector

Key Learning:

Embeddings represent meaning numerically.

---

## 4. Attention

Purpose:
Determine which words are important.

Example:

river bank
↓
Focus on "river"

money in bank
↓
Focus on "money"

Key Learning:

Attention helps the model understand context.

---

## 5. Transformer Layers

Purpose:
Repeatedly refine understanding.

Process Engineering Analogy:

Distillation Column
↓
Many Trays
↓
High Purity

Transformer
↓
Many Layers
↓
Deep Understanding

Key Learning:

Each layer improves understanding slightly.
Many layers together create sophisticated reasoning.

---

## 6. Language Model Head

Purpose:
Convert final vectors into word predictions.

Example:

"The capital of France is"

↓

Paris = 95%
London = 2%
Delhi = 1%

↓

Predict "Paris"

Key Learning:

The model predicts the most likely next token.

---

## Why GPT Works

GPT repeatedly performs:

Predict Next Token
↓
Add Token
↓
Predict Next Token
↓
Add Token

until the response is complete.

---

## Important Concepts for AI Applications

Tokens
→ Cost

Context Window
→ Memory during one request

Embeddings
→ Semantic Search & RAG

Attention
→ Context Understanding

Transformer
→ Language Understanding Engine

Language Model Head
→ Word Prediction

Hallucinations
→ Models predict likely text, not guaranteed truth

---

## Industrial AI Correlation

Embeddings
↓
Vector Databases
↓
RAG
↓
Document Assistants

Context Window
↓
Need for Chunking
↓
Need for RAG

Hallucinations
↓
Need for Tools
↓
Need for Documents
↓
Need for Validation

---

## One-Line Summary

LLMs convert text into vectors, use attention and transformer layers to build understanding, and repeatedly predict the next token to generate responses.


Text
↓
Tokens
↓
Embeddings
↓
Attention
↓
Transformer Layers
↓
Language Model Head
↓
Next Token
↓
Response