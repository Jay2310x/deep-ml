import numpy as np

def classify_critical_point(hessian, tol=1e-6):
    """
    Classify a critical point based on Hessian eigenvalues.

    Returns:
        -1  → local minimum  (all eigenvalues > 0)
         1  → local maximum  (all eigenvalues < 0)
         0  → saddle point   (mixed signs)
        None → inconclusive  (any eigenvalue ≈ 0 within tolerance)
    """
    H = np.array(hessian, dtype=float)
    
    # Compute eigenvalues
    eigenvalues = np.linalg.eigvals(H)
    
    # Check for near-zero eigenvalues
    if np.any(np.abs(eigenvalues) < tol):
        return None
    
    # Check signs
    if np.all(eigenvalues > 0):
        return -1  # Local minimum
    elif np.all(eigenvalues < 0):
        return 1   # Local maximum
    else:
        return 0   # Saddle point