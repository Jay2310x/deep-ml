import numpy as np

def n_step_td_prediction(
    episodes: list[list[tuple[int, float]]],
    n_states: int,
    n: int,
    gamma: float,
    alpha: float
) -> np.ndarray:
    """
    Perform n-step TD prediction to estimate state values.
    
    Args:
        episodes: List of episodes. Each episode is a list of (state, reward) tuples.
                  Reward is received after leaving the state.
        n_states: Total number of states.
        n: Number of steps for n-step return.
        gamma: Discount factor.
        alpha: Learning rate.
    
    Returns:
        Updated value function as a numpy array of size n_states.
    """
    
    V = np.zeros(n_states)

    for episode in episodes:
        T = len(episode)
        
        for t in range(T):
            state_t, _ = episode[t]
            
            # Compute n-step return
            G = 0.0
            for k in range(n):
                if t + k < T:
                    _, reward = episode[t + k]
                  