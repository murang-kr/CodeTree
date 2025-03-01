x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
grids = [[-1 for _ in range(2001)]for _ in range(2001)]
OFFSET = 1000

for i in range(2):
    a, b, c, d = x1[i]+OFFSET, y1[i]+OFFSET, x2[i]+OFFSET, y2[i]+OFFSET
    for j in range(a, c):
        for k in range(b, d):
            grids[j][k] = i

max_x = -1
min_x = 9999
max_y = -1
min_y = 9999
for i in range(x1[0]+OFFSET, x2[0]+OFFSET):
    for j in range(y1[0]+OFFSET, y2[0]+OFFSET):
        if grids[i][j] == 0:
            if i >= max_x and j >= max_y:
                max_x, max_y = i, j
            
            if i <= min_x and j <= min_y:
                min_x, min_y = i, j
    
if max_x == -1 and max_y == -1 and min_x == 9999 and min_y == 9999:
    print(0)
else:
    max_x += 1
    max_y += 1
    print((max_x-min_x)*(max_y-min_y))