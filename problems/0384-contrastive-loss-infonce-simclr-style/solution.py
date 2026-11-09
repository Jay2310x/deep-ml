import numpy as np

def contrastive_loss(embeddings: np.ndarray, temperature: float) -> float:
    """
    Compute the NT-Xent (SimCLR-style) contrastive loss.
    
    Args:
        embeddings: Array of shape (2N, d) where consecutive pairs
                    (2i, 2i+1) are positive pairs.
        temperature: Temperature scaling parameter (tau > 0).
    
    Returns:
        The mean contrastive loss as a float.
    """
    # Step 1: L2 normalize embeddings
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    z = embeddings / norms

    # Step 2: Cosine similarity matrix (2N x 2N)
    sim_matrix = np.dot(z, z.T)

    # Scale by temperature
    sim_matrix = sim_matrix / temperature

    N = sim_matrix.shape[0]

    # Mask self-similarity
    np.fill_diagonal(sim_matrix, -np.inf)

    losses = []

    for i in range(N):
        # Positive index (0↔1, 2↔3, ...)
        if i % 2 == 0:
            pos_idx = i + 1
        else:
            pos_idx = i - 1

        # Numerator