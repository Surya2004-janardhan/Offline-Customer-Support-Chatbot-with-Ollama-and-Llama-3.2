# Project Explanation: Offline Customer Support Chatbot

This document provides a deep dive into the technical architecture, workflow, and core definitions of the Offline Customer Support Chatbot project.

---

## 🔄 Project Workflow
The system follows a linear execution path to evaluate the performance of local LLMs in a customer service context.

1.  **Initialization**: The script (`chatbot.py`) loads the `OLLAMA_HOST` from environment variables (defaulting to `localhost` for local runs).
2.  **Prompt Loading**: It reads two text templates from the `prompts/` directory:
    - `zero_shot_template.txt`
    - `one_shot_template.txt`
3.  **Iteration**: The script loops through a predefined list of 20 e-commerce queries (e.g., tracking, returns, technical issues).
4.  **Inference**:
    - For each query, it formats a full prompt using the **Zero-Shot** template.
    - It sends an HTTP POST request to the **Ollama API**.
    - It repeats this for the **One-Shot** template.
5.  **Logging**: The results are formatted into a markdown table and appended to `eval/results.md`.
6.  **Human Evaluation**: A human (or agent) reviews the responses and assigns scores based on the **Scoring Rubric** in `results.md`.
7.  **Analysis**: The final averages and observations are recorded in `report.md`.

---

## 🛠️ Important Functions (in `chatbot.py`)

### `query_ollama(prompt)`
- **Purpose**: Communicates with the local Ollama server.
- **Logic**: Sends a JSON payload containing the `model` name and `prompt`.
- **Handling**: It uses `stream: False` to get the entire response at once rather than chunking it.

### `read_template(file_path)`
- **Purpose**: Utility to safely read prompt files.
- **Why?**: Keeps the prompting logic separate from the code, allowing for easy experimentation without modifying the script.

### `main()`
- **Purpose**: Orchestrator of the evaluation.
- **Logic**: It manages the file writing and the double-query loop (Zero-Shot vs. One-Shot) to ensure every query is tested under both conditions fairly.

---

## 📖 Key Definitions

| Term | Definition in this Project |
| :--- | :--- |
| **Ollama** | A tool that allows you to run open-source Large Language Models (LLMs) like Llama 3.2 locally on your own machine. |
| **Llama 3.2 (3B)** | Meta's 3-billion-parameter model. Lightweight enough for consumer CPUs but powerful for instruction following. |
| **Zero-Shot** | Asking the AI to perform a task without giving it any prior examples of "good" responses. |
| **One-Shot** | Providing the AI with exactly **one example** of a high-quality response to help it understand tone and format. |
| **Hallucination** | When an LLM confidently states something that is factually incorrect or makes up a procedure (e.g., fake account deletion steps). |
| **Inference** | The process where the AI model processes a prompt and generates a response. |
| **Endpoint** | The specific URL (`http://localhost:11434/api/generate`) where the chatbot sends its data to talk to Ollama. |

---

## 🏗️ Architecture Detail
Within **Docker**, the two services are isolated:
- `ollama`: Runs the model and listens on port 11434.
- `chatbot`: Runs the Python script and connects to the `ollama` container via the internal Docker network.

This ensures the system can be deployed anywhere with a single command without worrying about Python versions or missing model files.
