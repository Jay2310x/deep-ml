def gridworld_policy_evaluation(policy, gamma, threshold):
    size = 5
    V = [[0.0 for _ in range(size)] for _ in range(size)]
    
    terminals = {(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)}
    
    actions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    
    while True:
        delta = 0
        new_V = [row[:] for row in V]   # 🔥 copy for synchronous update
        
        for i in range(size):
            for j in range(size):
                
                if (i, j) in terminals:
                    continue
                
                new_v = 0
                
                for action, prob in policy[(i, j)].items():
                    di, dj = actions[action]
                    ni, nj = i + di, j + dj
                    
                    if ni < 0 or ni >= size or nj < 0 or nj >= size:
                        ni, nj = i, j
                    
                    reward = -1
             