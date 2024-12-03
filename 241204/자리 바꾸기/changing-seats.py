def count_sit(num):
    current_sits = list(range(1, N+1))
    visited = [num]
    i = 0
    while True:
        if num in swaps[i]:
            if swaps[i][0] != num:
                num = swaps[i][0]
            else:
                num = swaps[i][1]

            if num not in visited:
                visited.append(num)
        current_sits[swaps[i][0]-1], current_sits[swaps[i][1]-1] = (
            current_sits[swaps[i][1]-1],
            current_sits[swaps[i][0]-1],
        )
        i += 1
        if i == K:
            i = 0
        
        if current_sits == sits:
            break

    return len(visited)

N, K = map(int, input().split())
sits = list(range(1, N+1))
swaps = []

for i in range(K):
    swaps.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    print(count_sit(i))
