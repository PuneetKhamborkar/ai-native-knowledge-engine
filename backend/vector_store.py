from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory index
index = None
kdf_texts = []


def build_text(kdf):
    """
    Convert KDF into searchable semantic text
    """

    parts = []

    parts.append(kdf.get("intent", ""))

    if "requirements" in kdf:
        parts.extend(kdf["requirements"])

    if "context" in kdf:
        parts.extend(kdf["context"])

    if "rules" in kdf:
        parts.extend(kdf["rules"])

    if "api" in kdf:
        parts.append(str(kdf["api"]))

    return " ".join(parts)


def index_kdfs(kdfs):
    """
    Create FAISS index from KDFs
    """

    global index, kdf_texts

    texts = []
    for kdf in kdfs:
        text = build_text(kdf)
        texts.append(text)

    if not texts:
        print("⚠️ No KDFs to index")
        return

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    kdf_texts = texts

    print(f"✅ Indexed {len(texts)} KDFs")


def search_kdfs(query, top_k=3):
    """
    Search relevant KDFs using semantic similarity
    """

    global index, kdf_texts

    if index is None:
        print("⚠️ Index not initialized")
        return []

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for i in indices[0]:
        if i < len(kdf_texts):
            results.append(kdf_texts[i])

    return results