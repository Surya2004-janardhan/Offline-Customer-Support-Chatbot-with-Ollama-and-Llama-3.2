# chatbot.py
import requests
import json
import os

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

def query_ollama(prompt):
    """Sends a prompt to the Ollama API and returns the generated response."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return f"Error: Could not get a response from the model. Details: {e}"

def read_template(template_path):
    """Reads a prompt template from a file."""
    if not os.path.exists(template_path):
        return None
    with open(template_path, 'r') as f:
        return f.read()


def get_ecommerce_queries():
    """Returns the 20 adapted e-commerce customer queries."""
    return [
    "How do I track the shipping status of my recent order?",
    "My discount code is not working at checkout. Can you help?",
    "What is your return policy for international orders?",
    "I received the wrong item in my package. How do I exchange it?",
    "Can you help me reset my account password?",
    "Is this product available in a size medium?",
    "My credit card was charged twice for the same order.",
    "When will my backordered item finally ship?",
    "I need to change the shipping address on an order I just placed.",
    "Do you offer price matching if an item goes on sale after I buy it?",
    "Can you explain how your reward points system works?",
    "Why was my order canceled without any notification?",
    "How can I delete my account and remove my personal data?",
    "I received a defective product, how can I get a replacement?",
    "Is it possible to track the exact location of the delivery truck?",
    "Can I use two different promo codes on the same checkout?",
    "Which payment methods do you accept for international shipping?",
    "How long does it typically take for a refund to process to my bank?",
    "Can I change the email address associated with my account?",
    "Do you offer gift wrapping services for online orders?"
]

if __name__ == "__main__":
    queries = get_ecommerce_queries()
    zero_shot_template = read_template("prompts/zero_shot_template.txt")
    one_shot_template = read_template("prompts/one_shot_template.txt")

    # Ensure eval directory exists
    os.makedirs("eval", exist_ok=True)
    
    results_path = "eval/results.md"
    
    with open(results_path, "w") as f:
        # Initialize results file with header
        f.write("# Evaluation Results\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---------|----------------|------------------|----------|-----------------|-----------------|-------------------|\n")

        print(f"Loaded {len(queries)} e-commerce queries for evaluation.\n")
        print(f"Writing results to {results_path}\n")
        
        for i, query in enumerate(queries, 1):
            print(f"Query {i}: {query}")
            
            # Zero-Shot
            zero_shot_prompt = zero_shot_template.format(query=query)
            print("  Querying zero-shot...")
            zero_response = query_ollama(zero_shot_prompt).replace("\n", " ") # Ensure it fits in one table row
            f.write(f"| {i} | {query} | Zero-Shot | {zero_response} | | | |\n")
            print(f"  Zero-Shot Response: {zero_response[:50]}...\n")
            
            # One-Shot
            one_shot_prompt = one_shot_template.format(query=query)
            print("  Querying one-shot...")
            one_response = query_ollama(one_shot_prompt).replace("\n", " ") # Ensure it fits in one table row
            f.write(f"| {i} | {query} | One-Shot | {one_response} | | | |\n")
            print(f"  One-Shot Response: {one_response[:50]}...\n")

    print(f"\nEvaluation complete. Results saved to {results_path}")
