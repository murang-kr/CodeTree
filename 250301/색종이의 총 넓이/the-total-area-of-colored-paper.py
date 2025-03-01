n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
grids = [[0 for _ in range(201)]for _ in range(201)]
OFFSET = 100

for i in range(n):
    a, b = x[i]+OFFSET, y[i]+OFFSET
    for j in range(a, a+8):
        for k in range(b, b+8):
            grids[j][k] = 1

sum_val = 0
for row in grids:
    sum_val += sum(row)

print(sum_val)