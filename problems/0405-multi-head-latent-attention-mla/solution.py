import numpy as np

def multi_head_latent_attention(
    X: np.ndarray,
    W_dkv: np.ndarray,
    W_uk: np.ndarray,
    W_uv: np.ndarray,
    W_dq: np.ndarray,
    W_uq: np.ndarray,
    W_o: np.ndarray,
    n_heads: int
) -> tuple:
    """
    Perform Multi-Head Latent Attention (MLA).
    """

    # -----------------------------
    # 1️⃣ Basic shape information
    # -----------------------------
    seq_len, d_model = X.shape

    # Ensure d_model divisible by number of heads
    assert d_model % n_heads == 0, "d_model must be divisible by n_heads"

    d_head = d_model // n_heads   # dimension per head


    # -----------------------------
    # 2️⃣ Compress Keys & Values
    # -----------------------------
    # Compress input into low-dimensional latent
    c_kv = X @ W_dkv   # (seq_len, d_c_kv)

    # Reconstruct full Keys
    K = c_kv @ W_uk    # (seq_len, d_model)

    # Reconstruct full Values
    V = c_kv @ W_uv    # (seq_len, d_model)


    # -----------------------------
