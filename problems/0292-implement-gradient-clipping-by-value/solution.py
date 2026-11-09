import numpy as np # Import the library if you haven't already

def clip_gradients_by_value(gradients: np.ndarray, clip_value: float) -> np.ndarray:
    # Start with a copy of the original gradients array
    modified_gradients = gradients.copy()
    
    # Apply conditions using NumPy boolean masking
    # Where gradients > clip_value, set them to clip_value
    modified_gradients[modified_gradients > clip_value] = clip_value
    
    # Where gradients < -clip_value, set them to -clip_value
    modified_gradients[modified_gradients < -clip_value] = -clip_value
    
    return modified_gradients
