from sentence_transformers import SentenceTransformer
import numpy as np

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load notes
with open("notes.txt", "r", encoding="utf-8") as file:
    notes = [line.strip() for line in file if line.strip()]

# Convert notes to embeddings
note_embeddings = model.encode(notes)

def semantic_search(query):
    query_embedding = model.encode([query])
    
    similarities = np.dot(note_embeddings, query_embedding.T).flatten()
    best_match_index = np.argmax(similarities)
    
    return notes[best_match_index]

print("\nSemantic Search System using Endee Vector Architecture\n")

while True:
    user_query = input("Enter your question (or type 'exit'): ")
    
    if user_query.lower() == "exit":
        print("Goodbye!")
        break
    
    result = semantic_search(user_query)
    print("\nMost Relevant Note:")
    print(result)
    print()