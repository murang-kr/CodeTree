commands = input()

# Please write your code here.
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
dir_num = 0
x, y = 0, 0
cnt = 0
flag = True

for command in commands:
    if command == "F":
        x, y = x + dxs[dir_num], y + dys[dir_num]
    elif command == "R":
        dir_num = (dir_num + 1) % 4
    elif command == "L":
        dir_num = (dir_num + 3) % 4
    cnt += 1
    if x == 0 and y == 0:
        print(cnt)
        flag = False
        break

if flag:
    print(-1)