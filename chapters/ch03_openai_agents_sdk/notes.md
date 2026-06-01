1. Everything starts with Messages

2. System Prompt controls behavior

3. Context controls quality

4. Tools give real-world access

5. Structured output enables automation

6. Agent = LLM + Tools + Instructions

7. RAG will later inject plant knowledge

8. Multi-Agent will later split responsibilities



Example 1:
Text → LLM → Answer

Example 2:
Messages → LLM → Answer

Example 3:
System Prompt + User → LLM → Answer

Example 4:
Text + Image → LLM → Answer


##########
# Chapter 3 - Messages, Roles and Response Objects

## Objective

Learn how to communicate with an LLM using structured messages instead of a simple prompt.

---

## Key Components

### 1. Client

```python
client = OpenAI()
```

Purpose:

Creates a connection to OpenAI services.

Mental Model:

Python Application
→ OpenAI Client
→ OpenAI API
→ Model

---

### 2. Messages

```python
input=[
    {"role":"developer", ...},
    {"role":"user", ...}
]
```

Purpose:

Provide structured conversation context.

Mental Model:

Conversation =
Developer Instructions
+
User Question

---

### 3. Developer Role

```python
{
    "role":"developer",
    "content":"You are a senior process engineer..."
}
```

Purpose:

Controls model behavior.

Examples:

* Process Engineer
* ASU Specialist
* Cooling Tower Expert
* Maintenance Engineer
* Plant Operator Trainer

Key Learning:

Changing the role changes the style and depth of the answer.

This is the foundation of AI Agents.

---

### 4. User Role

```python
{
    "role":"user",
    "content":"Question"
}
```

Purpose:

Contains the actual request.

Examples:

* Explain compressor surge.
* Analyze cooling tower performance.
* Explain de-ethanizer operation.

---

### 5. Model

```python
model="gpt-5.2"
```

Purpose:

Selects the LLM used to generate the response.

---

### 6. Output Control

```python
max_output_tokens=20
```

Purpose:

Limits response length.

Useful for:

* Cost control
* Structured responses
* Production systems

---

### 7. Reasoning Effort

```python
reasoning={"effort":"low"}
```

Purpose:

Controls reasoning depth.

Possible values:

* low
* medium
* high

Tradeoff:

# Higher reasoning

# Better analysis

Higher cost and latency

---

## Understanding the Response Object

### Status

```python
response.status
```

Example:

completed

Purpose:

Indicates request success.

---

### Incomplete Details

```python
response.incomplete_details
```

Purpose:

Shows why generation stopped if incomplete.

Normally:

None

---

### Token Usage

```python
response.usage.total_tokens
```

Purpose:

Measures API consumption.

Important for:

* Cost tracking
* Performance monitoring
* Production systems

---

### Output Text

Simple:

```python
response.output_text
```

Detailed:

```python
response.output[0].content[0].text
```

Both return the generated answer.

Prefer:

```python
response.output_text
```

for most applications.

---

## Most Important Learning

The quality of the answer is influenced by:

Role
+
Instructions
+
Question
+
Model

not just the user question.

---

## Agent Design Insight

Future AI Agents will primarily be built using:

Developer Instructions
+
User Input
+
Context
+
Tools
+
LLM

This example demonstrates the first two components:

Developer Instructions
+
User Input

---

## Industrial AI Example

ASU Assistant:

Developer:

"You are a senior Air Separation Unit engineer."

User:

"Why is oxygen purity dropping?"

Cooling Tower Copilot:

Developer:

"You are a cooling water specialist."

User:

"Why is cooling tower approach temperature increasing?"

Same LLM.
Different role.
Different behavior.

---

## Key Takeaway

Messages are more powerful than simple prompts.

The developer role is used to create specialized AI assistants and forms the basis of Agentic AI systems.
  

  Example 1
Text
↓
Answer

Example 2
Messages
↓
Answer

Example 3
Developer Role
+
User Question
↓
Specialized Answer

Example 4
Text
+
Image
↓
Vision Analysis



########
# Chapter 3 - Streaming Responses

## Objective

Display text as it is generated instead of waiting for the complete response.

---

## Normal Response

Request
↓
Wait
↓
Full Response
↓
Display

---

## Streaming Response

Request
↓
Chunk
↓
Chunk
↓
Chunk
↓
Display Immediately

---

## Key Parameter

```python
stream=True
```

Enables streaming mode.

---

## Processing Stream

```python
for event in response:
```

Receives chunks as they arrive.

---

## Text Chunks

```python
event.type == "response.output_text.delta"
```

Indicates text content.

---

## Actual Text

```python
event.delta
```

Contains the generated text fragment.

---

## Display

```python
print(event.delta, end="", flush=True)
```

end=""

Avoids line breaks.

flush=True

Displays text immediately.

---

## Benefits

* Better user experience
* Faster perceived response time
* Useful for chat interfaces
* Useful for AI assistants

---

## Industrial Use Cases

* ASU Assistant
* Cooling Tower Copilot
* Plant Chatbot
* Maintenance Assistant

---

## Key Learning

Streaming changes how responses are delivered, not how answers are generated.

The model is the same.

Only the delivery mechanism changes.


Multimodal AI

Input:
Text + Image

Output:
Text Response

Key Learning:
LLMs can analyze images in addition to text.

Applications:
- Leak detection
- Equipment inspection
- P&ID analysis
- Safety audits
- Maintenance support

Mental Model:
Image + Question → Reasoning → Answer


##

# Chapter 3 - Streaming Responses

## Objective

Display text as it is generated instead of waiting for the complete response.

---

## Normal Response

Request
↓
Wait
↓
Full Response
↓
Display

---

## Streaming Response

Request
↓
Chunk
↓
Chunk
↓
Chunk
↓
Display Immediately

---

## Key Parameter

```python
stream=True
```

Enables streaming mode.

---

## Processing Stream

```python
for event in response:
```

Receives chunks as they arrive.

---

## Text Chunks

```python
event.type == "response.output_text.delta"
```

Indicates text content.

---

## Actual Text

```python
event.delta
```

Contains the generated text fragment.

---

## Display

```python
print(event.delta, end="", flush=True)
```

end=""

Avoids line breaks.

flush=True

Displays text immediately.

---

## Benefits

* Better user experience
* Faster perceived response time
* Useful for chat interfaces
* Useful for AI assistants

---

## Industrial Use Cases

* ASU Assistant
* Cooling Tower Copilot
* Plant Chatbot
* Maintenance Assistant

---

## Key Learning

Streaming changes how responses are delivered, not how answers are generated.

The model is the same.

Only the delivery mechanism changes.


##################3.2A:3.2

# Building Agents using OpenAI Agents SDK

## Agent Definition

Agent = LLM + Instructions + Tools

---

## Traditional LLM

User
↓
LLM
↓
Answer

---

## Agent

User
↓
Agent
↓
LLM
↓
Tools
↓
Answer

---

## Why Agents Exist

LLMs alone cannot:

* Access live data
* Query databases
* Perform external actions
* Access enterprise systems

Agents solve this limitation.

---

## Examples of Tools

* Search
* Calculator
* Database
* Weather API
* File Retrieval
* Plant Historian

---

## Industrial Examples

ASU Assistant

Tools:

* Historian
* SOP Documents
* Alarm History

Cooling Tower Copilot

Tools:

* Water Chemistry Data
* Inspection Reports
* Performance Calculations

Heat Exchanger Assistant

Tools:

* Fouling Calculations
* Inspection Data
* Performance Trends

---

## Key Learning

An Agent is not a smarter LLM.

An Agent is an LLM that can use tools and follow specialized instructions.


######
# First Agent Example

## Objective

Understand how an Agent differs from a normal LLM call.

---

## Traditional LLM

User
↓
LLM
↓
Answer

---

## Agent

User
↓
Agent
↓
Tool
↓
LLM
↓
Answer

---

## Agent Components

Agent =

* Name
* Instructions
* Model
* Tools

---

## Tool

A Python function that the Agent is allowed to call.

Example:

```python
@function_tool
def convert_temperature(...)
```

The decorator exposes the function to the Agent.

---

## Agent Creation

```python
agent = Agent(...)
```

Creates an Agent with:

* Instructions
* Model
* Tools

---

## Runner

```python
Runner.run_sync(...)
```

Executes the Agent.

---

## Internal Flow

User Question
↓
Agent Receives Query
↓
Agent Selects Tool
↓
Tool Executes
↓
Result Returned
↓
Final Answer Generated

---

## Key Learning

Agents do not replace tools.

Agents decide when and how to use tools.

---

## Industrial AI Connection

Future tools may include:

* Historian Access
* Plant Documents
* Calculators
* Databases
* Weather APIs
* Maintenance Systems

The temperature converter demonstrates the same architecture used by enterprise AI agents.


# First Agent with Tool

## Flow

User Question
↓
Agent
↓
LLM decides if tool is needed
↓
Tool executes
↓
Tool returns result
↓
LLM formats final answer
↓
User

---

## Key Components

@function_tool

Makes a Python function available to the Agent as a tool.

Agent

Contains:

* Instructions
* Model
* Tools

Runner.run_sync()

Starts and executes the Agent.

---

## Key Learning

The LLM does not execute Python code.

The LLM decides:

* Which tool to use
* What arguments to pass

The SDK executes the tool and returns the result.

---

## Mental Model

Tools compute.
LLMs communicate.
Agents coordinate.

---

## Takeaway

Agent = LLM + Instructions + Tools
