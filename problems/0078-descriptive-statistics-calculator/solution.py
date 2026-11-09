import numpy as np
from scipy import stats

def descriptive_statistics(data: list | np.ndarray) -> dict:
    arr = np.asarray(data)
    
    # Central Tendency
    mean = float(np.mean(arr))
    median = float(np.median(arr))
    # stats.mode returns ModeResult(mode=array([...]), count=array([...]))
    mode = float(stats.mode(arr, keepdims=False).mode)
    
    # Dispersion (Population Variance uses ddof=0)
    variance = float(np.var(arr, ddof=0))
    standard_deviation = float(np.std(arr, ddof=0))
    
    # Percentiles
    p25 = float(np.percentile(arr, 25))
    p50 = float(np.percentile(arr, 50))
    p75 = float(np.percentile(arr, 75))
    iqr = p75 - p25
    
    return {
        'mean': round(mean, 4),
        'median': round(median, 4),
        'mode': round(mode, 4),
        'variance': round(variance, 4),
        'standard_deviation': round(standard_deviation, 4),
        '25th_percentile': round(p25, 4),
        '50th_percentile': round(p50, 4),
        '75th_percentile': round(p75, 4),
        'interquartile_range': round(iqr, 4)
    }