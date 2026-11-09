import numpy as np

def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Gaussian Naive Bayes implementation from scratch.
    
    Parameters:
    X_train : np.ndarray (n_samples, n_features)
    y_train : np.ndarray (n_samples,)
    X_test  : np.ndarray (m_samples, n_features)
    
    Returns:
    np.ndarray of predicted class labels
    """
    
    epsilon = 1e-9  # for numerical stability
    classes = np.unique(y_train)
    n_features = X_train.shape[1]
    
    # Store parameters
    priors = {}
    means = {}
    variances = {}
    
    # -----------------------------
    # TRAINING PHASE
    # -----------------------------
    
    for c in classes:
        X_c = X_train[y_train == c]
        
        # Prior probability
        priors[c] = X_c.shape[0] / X_train.shape[0]
        
        # Mean and variance per feature
        means[c] = np.mean(X_c, axis=0)
        variances[c] = np.var(X_c, axis=0) + epsilon
    
    # -----------------------------
    # PREDICT