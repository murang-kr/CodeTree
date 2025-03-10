n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0] #E, N, W, S
dir_num = 0
x = y = n//2
step, cnt, num = 1, 0, 2
grid[x][y] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

while num < n*n:
    for _ in range(step):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        if not in_range(x, y):
            break
        grid[x][y] = num
        num += 1
    dir_num = (dir_num+1)%4
    cnt += 1
    if cnt == 2:
        step += 1
        cnt = 0

for row in grid:
    for elem in row:
        print(elem, end = " ")
    print()