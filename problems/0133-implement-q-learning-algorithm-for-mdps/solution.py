import numpy as np

def q_learning(num_states, num_actions, P, R, terminal_states,
               alpha, gamma, epsilon, num_episodes):
    
    Q = np.zeros((num_states, num_actions))
    terminal_states = set(terminal_states)

    for _ in range(num_episodes):

        # start from random non-terminal state
        state = np.random.choice(
            [s for s in range(num_states) if s not in terminal_states]
        )

        while state not in terminal_states:

            # epsilon-greedy action selection
            if np.random.rand() < epsilon:
                action = np.random.randint(num_actions)
            else:
                action = np.argmax(Q[state])

            # sample next state
            next_state = np.random.choice(
                num_states, p=P[state, action]
            )

            reward = R[state, action]

            # Q-learning update
            Q[state, action] += alpha * (
                reward + gamma * np.max(Q[next_state]) - Q[state, act