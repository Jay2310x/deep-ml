import math

def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    # Your code here
    bc = math.comb(n,k)
    success_term = math.pow(p,k)
    failur_term = math.pow(1-p,n-k)
    return bc*success_term*failur_term