n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {'R': 0, 'D': 1, 'U': 2, 'L': 3}
dir_num = mapper[d]
x, y = r-1, c-1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(t-1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
    x, y = x + dxs[dir_num], y + dys[dir_num]

print(x+1, y+1)