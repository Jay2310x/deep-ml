import numpy as np

def calculate_correlation_matrix(X, Y=None):
    # Convert to numpy array
    X = np.array(X)
    
    if Y is None:
        Y = X
    else:
        Y = np.array(Y)
    
    # Center the data (subtract mean)
    X_mean = X - np.mean(X, axis=0)
    Y_mean = Y - np.mean(Y, axis=0)
    
    # Compute covariance matrix
    covariance = (X_mean.T @ Y_mean) / (X.shape[0] - 1)
    
    # Compute standard deviations
    std_X = np.std(X, axis=0, ddof=1)
    std_Y = np.std(Y, axis=0, ddof=1)
    
    # Outer product of standard deviations
    std_outer = np.outer(std_X, std_Y)
    
    # Correlation matrix
    correlation = covariance / std_outer
    
    return correlation