N, T = map(int, input().split())
string = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # N, E, S, W
dir_num = 0
x = y = N//2
sum_val = board[x][y]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

for i in range(T):
    if string[i] == "F":
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if not in_range(nx, ny):
            continue
        x, y = nx, ny
        sum_val += board[x][y]
    elif string[i] == "R":
        dir_num = (dir_num+1)%4
    elif string[i] == "L":
        dir_num = (dir_num+3)%4

print(sum_val)