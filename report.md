# Project Report: Offline Customer Support Chatbot Evaluation

## 1. Introduction
This report documents the development and evaluation of an offline customer support chatbot powered by Ollama and the Llama 3.2 (3B) model. The goal was to compare the effectiveness of different prompting techniques in responding to common e-commerce customer queries.

## 2. Methodology
The evaluation was conducted using 20 adapted queries from the Ubuntu Dialogue Corpus, modified for an e-commerce context. Two prompting methods were compared:
- **Zero-Shot:** A generic template with basic persona instructions.
- **One-Shot:** A targeted template including a high-quality example of a return policy response and strict policy instructions.

The system was implemented in Python, interfacing with a local Ollama server. Responses were manually scored on a scale of 1 to 5 for Relevance, Coherence, and Helpfulness.

## 3. Results Analysis
The evaluation revealed a significant performance gap between the two prompting methods:

| Metric | Zero-Shot (Avg) | One-Shot (Avg) |
|--------|-----------------|----------------|
| Relevance | 3.0 | 5.0 |
| Coherence | 4.0 | 5.0 |
| Helpfulness | 3.0 | 5.0 |

### Observations:
- **Zero-Shot:** While coherent, responses were often too generic. They lack specific actionable details such as placeholder URLs or detailed step-by-step instructions.
- **One-Shot:** The inclusion of a single high-quality example dramatically improved the model's ability to follow a specific "helpful and professional" persona. The responses were more detailed, providing specific links and departmental contacts (e.g., `replacement@example.com`).
