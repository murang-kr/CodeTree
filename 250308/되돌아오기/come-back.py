N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {'E': 0, 'S': 1, 'N': 2, 'W': 3}
x, y = 0, 0
cnt = 0

for i in range(N):
    flag = False
    dir_num = mapper[dir[i]]
    for j in range(dist[i]):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        cnt += 1
        if x == 0 and y == 0:
            flag = True
            print(cnt)
            break
    if flag:
        break

if not flag:
    print(-1)