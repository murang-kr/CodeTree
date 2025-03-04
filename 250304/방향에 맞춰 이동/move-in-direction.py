n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1] # E=0, W=1, S=2, N=3
cur_loc = (0, 0)
for i in range(n):
    direction_num = None
    if dir[i] == "E":
        direction_num = 0
    elif dir[i] == "W":
        direction_num = 1
    elif dir[i] == "S":
        direction_num = 2
    elif dir[i] == "N":
        direction_num = 3

    cur_loc = (cur_loc[0]+dx[direction_num]*dist[i], cur_loc[1]+dy[direction_num]*dist[i])

print(cur_loc[0], cur_loc[1])