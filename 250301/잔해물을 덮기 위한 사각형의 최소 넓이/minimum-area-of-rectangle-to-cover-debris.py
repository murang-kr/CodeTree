x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
grids = [[0 for _ in range(2001)]for _ in range(2001)]
OFFSET = 1000

for i in range(2):
    a, b, c, d = x1[i]+OFFSET, y1[i]+OFFSET, x2[i]+OFFSET, y2[i]+OFFSET
    for j in range(a, c):
        for k in range(b, d):
            if i == 0:
                grids[j][k] = 1
            else:
                grids[j][k] = 0

max_x, max_y, min_x, min_y = -1, -1, 9999, 9999

for i in range(x1[0]+OFFSET, x2[0]+OFFSET):
    for j in range(y1[0]+OFFSET, y2[0]+OFFSET):
        if grids[i][j] == 1:
            if i > max_x:
                max_x = i
            if i < min_x:
                min_x = i
            if j > max_y:
                max_y = j
            if j < min_y:
                min_y = j

if max_x == -1 and max_y == -1 and min_x == 9999 and min_y == 9999:
    print(0)
else:
    max_x += 1
    max_y += 1
    print((max_x-min_x)*(max_y-min_y))