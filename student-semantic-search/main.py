from sentence_transformers import SentenceTransformer
import numpy as np

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# LOAD NOTES
# -----------------------------
with open("notes.txt", "r", encoding="utf-8") as file:
    full_text = file.read()

# Split into chunks (paragraph-based)
chunks = [para.strip() for para in full_text.split("\n") if para.strip()]

# Convert to embeddings
embeddings = model.encode(chunks)

# Normalize for cosine similarity
embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)


# -----------------------------
# SEMANTIC SEARCH FUNCTION
# -----------------------------
def semantic_search(query, top_k=3):
    query_embedding = model.encode([query])
    query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)

    similarities = np.dot(embeddings, query_embedding.T).flatten()

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = [(chunks[i], similarities[i]) for i in top_indices]
    return results


# -----------------------------
# INTERACTIVE LOOP
# -----------------------------
print("\n=== AI Study Assistant (Vector-Based Retrieval) ===\n")

while True:
    query = input("Ask your question (or type 'exit'): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    results = semantic_search(query)

    print("\nTop Relevant Answers:\n")
    for answer, score in results:
        print(f"Similarity Score: {score:.4f}")
        print(f"- {answer}")
        print("-" * 60)