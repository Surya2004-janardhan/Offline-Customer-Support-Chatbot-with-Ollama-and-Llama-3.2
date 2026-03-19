# Setup and Run Instructions

## 1. Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running.
- Llama 3.2 model downloaded: `ollama pull llama3.2:3b`

## 2. Installation
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 3. Running the Chatbot
To run the automated evaluation and generate responses:
```bash
python3 chatbot.py
```
Results will be saved to `eval/results.md`.
