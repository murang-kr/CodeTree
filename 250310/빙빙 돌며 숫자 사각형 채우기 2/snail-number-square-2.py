n, m = map(int, input().split())

# Please write your code here.
grid = [[0 for _ in range(m)] for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] #S, E, N, W
dir_num = 0
x, y = 0, 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(1, n*m+1):
    grid[x][y] = i
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    x, y = x + dxs[dir_num], y + dys[dir_num]

for row in grid:
    for elem in row:
        print(elem, end = " ")
    print()