import numpy as np

def local_response_normalization(x, n=5, k=2.0, alpha=1e-4, beta=0.75):
    """
    Apply Local Response Normalization (LRN) across channels.

    Parameters:
        x     : Input tensor of shape (N, C, H, W)
        n     : Number of neighboring channels (window size)
        k     : Bias term
        alpha : Scaling parameter
        beta  : Exponent

    Returns:
        Normalized tensor of same shape as input
    """

    N, C, H, W = x.shape
    output = np.zeros_like(x)

    # Pad squared values along channel dimension
    half_n = n // 2
    squared = x ** 2

    # Pad channel dimension (axis=1)
    padded = np.pad(
        squared,
        ((0, 0), (half_n, half_n), (0, 0), (0, 0)),
        mode='constant'
    )

    # Compute normalization
    for c in range(C):
        # Sum over local window in channel dimension
        local_sum = np.sum(padded[:, c:c+n, :, :], axis=1)

        # Apply normalization formula
        output[:, c, :, :] = x[:, c, :, :] / 