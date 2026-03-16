from datasets import load_dataset

def fetch_data():
    # Load the Ubuntu Dialogue Corpus
    dataset = load_dataset("rguo12/ubuntu_dialogue_corpus", "v2.0")
    
    # Extract the 'train' split which contains the dialogues
    train_data = dataset['train']
    print(f"Successfully loaded {len(train_data)} dialogues.")
    return train_data

if __name__ == "__main__":
    fetch_data()
