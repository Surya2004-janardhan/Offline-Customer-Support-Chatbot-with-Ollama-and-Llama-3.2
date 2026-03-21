# Project Report: Offline Customer Support Chatbot Evaluation

## 1. Introduction
This report documents the development and evaluation of an offline customer support chatbot powered by Ollama and the Llama 3.2 (3B) model. The goal was to compare the effectiveness of different prompting techniques in responding to common e-commerce customer queries.

## 2. Methodology
The evaluation was conducted using 20 adapted queries from the Ubuntu Dialogue Corpus, modified for an e-commerce context. Two prompting methods were compared:
- **Zero-Shot:** A generic template with basic persona instructions.
- **One-Shot:** A targeted template including a high-quality example of a return policy response and instructions.

The system was implemented in Python, interfacing with a local Ollama server. Responses were manually scored on a scale of 1 to 5 for Relevance, Coherence, and Helpfulness.

## 3. Results Analysis
The re-evaluation with a more critical lens shows that **Zero-Shot** models tend to over-promise or "hallucinate" capability (e.g., claiming they can change an email or delete an account directly) without having the back-end integration.

| Metric | Zero-Shot (Avg) | One-Shot (Avg) |
|--------|-----------------|----------------|
| Relevance | 4.7 | 4.8 |
| Coherence | 4.9 | 5.0 |
| Helpfulness | 3.3 | 4.5 |

### Observations:
- **Zero-Shot:** While highly coherent and polite, it suffers from "over-helpful hallucinations." For example, it frequently provided specific step-by-step instructions for account deletion or email changes that were purely guessed, as the model has no knowledge of the actual website interface. This is a high-risk behavior for customer support.
- **One-Shot:** The provided example significantly grounded the model. It was much more likely to acknowledge its limitations (e.g., "I don't have information about...") or direct the user to a real department, which is safer and more realistic for a production deployment.
- **Conclusion:** One-shot prompting is critical not just for establishing tone, but for **risk management**. It prevents the model from making up non-existent procedures that would frustrate customers.

## 4. Final Conclusion
The evaluation demonstrated that while Llama 3.2 3B is remarkably instruction-tuned, one-shot prompting is essential to keep the model grounded and prevent it from "hallucinating" system-specific procedures.

## 5. Limitations
- **Model Size:** The 3B model is efficient but follows complex constraints slightly less reliably than larger models.
- **Context Gap:** Without RAG (Retrieval-Augmented Generation), the model must rely on its pre-training or guessed procedures for specific company policies.
