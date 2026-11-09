import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a, b = matrix[0]
    c, d = matrix[1]
    
    det = (a * d) - (b * c)
    if det == 0:
        return None
        
    # Pass the list INSIDE np.array(...)
    mat = np.array([[d, -b], [-c, a]])
    
    # Divide and convert back to Python list
    return (mat / det).tolist()