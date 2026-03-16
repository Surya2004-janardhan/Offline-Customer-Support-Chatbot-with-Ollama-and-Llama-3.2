# chatbot.py

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
    "How long does it typically take for a refund to process to my bank?"
]

if __name__ == "__main__":
    queries = get_ecommerce_queries()
    print(f"Loaded {len(queries)} e-commerce queries for evaluation.")
