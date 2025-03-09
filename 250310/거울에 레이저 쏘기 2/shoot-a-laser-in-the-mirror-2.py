n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
dxr, dyr = [0, 1, 0, -1], [1, 0, -1, 0] #E, S, W, N
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] #S, W, N, E
rotate_num = 0
dir_num = (k-1)//n
x, y = 0, 0
cnt = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(k-1):
    nx, ny = x + dxr[rotate_num], y + dyr[rotate_num]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        rotate_num += 1

while True:
    if grid[x][y] == "/":
        dir_num = int(dir_num + (-1) ** dir_num)
    else:
        dir_num = 3 - dir_num
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    cnt += 1
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        break

print(cnt)