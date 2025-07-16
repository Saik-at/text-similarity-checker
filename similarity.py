from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the MiniLM model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1, text2):
    """
    Computes cosine similarity between two text inputs.
    """
    embeddings = model.encode([text1, text2])
    similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(similarity_score * 100, 2)  # return as percentage
