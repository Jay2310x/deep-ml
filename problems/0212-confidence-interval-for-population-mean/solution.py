import numpy as np
from scipy import stats

def confidence_interval(data: list[float], confidence_level: float = 0.95) -> dict:
    n = len(data)
    mean = float(np.mean(data))
    
    # Sample standard deviation (ddof=1 for sample) and standard error
    std_dev = np.std(data, ddof=1)
    standard_error = float(std_dev / np.sqrt(n))
    
    # Critical value from t-distribution
    df = n - 1
    alpha = 1.0 - confidence_level
    t_critical = stats.t.ppf(1 - alpha / 2, df)
    
    # Margin of error and bounds
    margin_of_error = float(t_critical * standard_error)
    lower_bound = float(mean - margin_of_error)
    upper_bound = float(mean + margin_of_error)
    
    return {
        'mean': round(mean, 4),
        'standard_error': round(standard_error, 4),
        'margin_of_error': round(margin_of_error, 4),
        'lower_bound': round(lower_bound, 4),
        'upper_bound': round(upper_bound, 4),
        'confidence_level': confidence_level
    }