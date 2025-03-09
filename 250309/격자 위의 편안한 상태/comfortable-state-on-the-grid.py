n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
grid = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1] #E, S, N, W

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(m):
    x, y = points[i][0]-1, points[i][1]-1
    grid[x][y] = 1
    cnt = 0
    for j in range(4):
        nx, ny = x + dxs[j], y + dys[j]
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
