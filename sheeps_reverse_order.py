def reverse_sheeps(sheeps, B, W):
    empty_space = B
    i = 0
    while i < W:
        empty_space = B + i
    
        j = 0
        # loop 4 times
        for j in range(0,4):
            sheeps[empty_space], sheeps[empty_space + 1] = sheeps[empty_space + 1], sheeps[empty_space]
            empty_space += 1
            sheeps[empty_space], sheeps[empty_space - 2] = sheeps[empty_space - 2], sheeps[empty_space]
            empty_space -= 2
            
        
        if i == W-1 :
            sheeps[empty_space], sheeps[empty_space + 1] = sheeps[empty_space + 1], sheeps[empty_space]
            empty_space += 1
        else:
            k = 0
            # loop 5 times
            for k in range(0,5):
                sheeps[empty_space], sheeps[empty_space + 1] = sheeps[empty_space + 1], sheeps[empty_space]
                empty_space += 1
        i += 1
    return sheeps
