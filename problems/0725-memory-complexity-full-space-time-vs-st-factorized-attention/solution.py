def attention_memory(T: int, H: int, W: int, num_heads: int, bytes_per_element: int) -> list:
    """
    Compute memory (in bytes) of attention score tensors for full space-time
    attention and for space-time factorized attention.
    """
    N = T * H * W
    S = H * W
    
    # Full space-time attention score tensor memory
    full_bytes = num_heads * (N ** 2) * bytes_per_element
    
    # Space-time factorized attention score tensor memory
    # Spatial attention: T matrices of size (S x S) per head
    # Temporal attention: S matrices of size (T x T) per head
    factorized_bytes = num_heads * (T * (S ** 2) + S * (T ** 2)) * bytes_per_element
    
    return [full_bytes, factorized_bytes]