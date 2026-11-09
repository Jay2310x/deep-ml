import numpy as np

def thanksgiving_dish_predictor(preference_scores: list[float]) -> list[float]:
    """
    Predict the probability of choosing each Thanksgiving dish using softmax.
    """
    
    scores = np.array(preference_scores)
    
    # Numerical stability trick
    scores = scores - np.max(scores)
    
    exp_scores = np.exp(scores)
    probabilities = exp_scores / np.sum(exp_scores)
    
    return probabilities.tolist()
