x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
grids = [[-1 for _ in range(2001)]for _ in range(2001)]
OFFSET = 1000

for i in range(3):
    a, b, c, d = x1[i]+OFFSET, y1[i]+OFFSET, x2[i]+OFFSET, y2[i]+OFFSET
    for j in range(a, c):
        for k in range(b, d):
            grids[j][k] = i

sum_val = 0
for row in grids:
    sum_val += row.count(0) + row.count(1)

print(sum_val)