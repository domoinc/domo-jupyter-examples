> **Domo AI Pro Operations & Processing** — AI services consume credits as described on [Domo's online consumption terms](https://www.domo.com/consumption-terms). See your instance's Rate Card under Admin > Company Settings > Credit Utilization.

# AI Services in Jupyter

This directory contains example notebooks for every AI service available through `domojupyter.ai`. Examples are organized by category. Each notebook is self-contained and progressively covers basic through advanced usage.

**Setup:** In any notebook, import the library with:
```python
import domojupyter.ai as ai
```

> **Note:** Example files are read-only. Copy the code into your own workspace notebook to run it.

---

## Text Generation

*Services that generate, transform, or continue text.*

| Notebook | Function | Description |
|---|---|---|
| [text-generation/text-generation.ipynb](text-generation/text-generation.ipynb) | `ai.generate_text()` | Generate text from a prompt. Supports prompt templates, system messages, structured output, and reasoning. |
| [text-generation/text-summarization.ipynb](text-generation/text-summarization.ipynb) | `ai.summarize()` | Summarize long text. Control output style, length, and chunking for large documents. |
| [text-generation/chat-completion.ipynb](text-generation/chat-completion.ipynb) | `ai.chat_completion()` | Single or multi-turn chat. Pass prior conversation history to maintain context. |
| [text-generation/messages.ipynb](text-generation/messages.ipynb) | `ai.messages()` | Full messages-style conversation with role-tagged turns. Supports extended reasoning. |

---

## Data & Formulas

*Services that work with Domo datasets and calculated fields.*

| Notebook | Function | Description |
|---|---|---|
| [data-and-formulas/text-to-sql.ipynb](data-and-formulas/text-to-sql.ipynb) | `ai.text_to_sql()` | Convert natural language questions to SQL. Accepts a schema definition, a connected dataset alias, or a pandas DataFrame. |
| [data-and-formulas/text-to-beastmode.ipynb](data-and-formulas/text-to-beastmode.ipynb) | `ai.text_to_beast_mode()` | Generate Domo Beast Mode (calculated field) formulas from plain English descriptions. |

---

## Tools & Agents

*Services that let the model use tools or plan multi-step tasks.*

| Notebook | Function | Description |
|---|---|---|
| [tools-and-agents/tool-calling.ipynb](tools-and-agents/tool-calling.ipynb) | `ai.tool_calling()` | Give the model a set of tools it can invoke. The model decides which tool to call and with what arguments. |

---

## Vision

*Services that understand image content.*

| Notebook | Function | Description |
|---|---|---|
| [vision/image-to-text.ipynb](vision/image-to-text.ipynb) | `ai.image_to_text()` | Describe, analyze, or extract structured data from images. Accepts local files or URLs. |

---

## Embeddings

*Services that produce vector representations of content.*

| Notebook | Function | Description |
|---|---|---|
| [embeddings/text-embedding.ipynb](embeddings/text-embedding.ipynb) | `ai.embedding()` | Embed one or more text strings. Use embeddings for semantic search, similarity scoring, and clustering. |
| [embeddings/image-embedding.ipynb](embeddings/image-embedding.ipynb) | `ai.image_embedding()` | Embed an image from a local file or URL. |

---

## Classification & Sentiment

*Services that categorize or score text.*

| Notebook | Function | Description |
|---|---|---|
| [classification-and-sentiment/classification.ipynb](classification-and-sentiment/classification.ipynb) | `ai.classification()` | Classify text into one or more labels. Supports single-label and multi-label modes. |
| [classification-and-sentiment/sentiment.ipynb](classification-and-sentiment/sentiment.ipynb) | `ai.sentiment()` | Analyze sentiment of text. Pass topics for targeted per-topic sentiment. |

---

## Common Parameters

Most services accept these shared optional parameters:

| Parameter | Type | Description |
|---|---|---|
| `model` | `str` | ID of a specific model. Omit to use the Domo default. |
| `system` | `str` | System message to set context or persona for the model. |
| `temperature` | `float` | Sampling temperature (0.0–1.0 for most services, up to 2.0 for chat). Lower = more deterministic. |
| `max_tokens` / `maxTokens` | `int` | Maximum tokens to generate in the response. |
| `prompt_template` | `PromptTemplate` | Custom prompt template using `${variable}` placeholders. |
| `parameters` | `dict` | Values for `${variable}` placeholders in a prompt template. |
| `response_format` | `dict` | Request structured JSON output: `{"type": "JSON", "schema": {...}}` |
| `reasoning_config` | `dict` | Enable extended reasoning: `{"enabled": True, "budgetTokens": 2000}` |
