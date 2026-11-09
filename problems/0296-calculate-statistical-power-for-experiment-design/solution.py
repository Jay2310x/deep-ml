import math

def calculate_power(effect_size: float, sample_size_per_group: int, alpha: float = 0.05, two_tailed: bool = True) -> float:
    """
    Calculate statistical power for a two-sample z-test.
    """
    # 1. Standard Normal Cumulative Distribution Function (CDF) using erf
    def normal_cdf(x: float) -> float:
        return 0.5 * (1.0 + math.erf(x / math.sqrt(2)))

    # 2. Inverse Standard Normal CDF (Quantile function) for Z_critical
    def normal_ppf(p: float) -> float:
        # Abramowitz and Stegun approximation for inverse normal CDF
        if p <= 0 or p >= 1:
            raise ValueError("Probability p must be between 0 and 1.")
        
        # Take advantage of symmetry around 0.5
        if p < 0.5:
            return -normal_ppf(1.0 - p)
        
        t = math.sqrt(-2.0 * math.log(1.0 - p))
        
        # Rational approximation coefficients
        c0, c1, c2 = 2.515517, 0.802853, 0.010328
        d1, d2, d3 = 1.432788, 0.189269, 0.001308
        
        z = t - ((c2 * t + c1) * t + c0) / (((d3 * t + d2) * t + d1) * t + 1.0)
        return z

    # 3. Calculate Non-Centrality Parameter (Shift)
    # shift = d * sqrt(n / 2)
    shift = effect_size * math.sqrt(sample_size_per_group / 2.0)

    # 4. Determine Critical Z-Value based on alpha and tail type
    if two_tailed:
        # Alpha is split across both tails: right tail area is 1 - alpha/2
        z_crit = normal_ppf(1.0 - alpha / 2.0)
        # Power is probability of falling beyond +z_crit OR below -z_crit under alternative hypothesis
        power = (1.0 - normal_cdf(z_crit - shift)) + normal_cdf(-z_crit - shift)
    else:
        # One-tailed test: right tail area is 1 - alpha
        z_crit = normal_ppf(1.0 - alpha)
        # Power is probability of exceeding z_crit under alternative distribution
        power = 1.0 - normal_cdf(z_crit - shift)

    # 5. Round to 4 decimal places as requested
    return round(power, 4)
    