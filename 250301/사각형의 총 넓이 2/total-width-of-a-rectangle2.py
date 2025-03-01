n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
grids = [[0 for _ in range(201)]for _ in range(201)]
OFFSET = 100

for i in range(n):
    a, b, c, d = x1[i]+OFFSET, y1[i]+OFFSET, x2[i]+OFFSET, y2[i]+OFFSET
    for j in range(a, c):
        for k in range(b, d):
            grids[j][k] = 1

sum_val = 0
for row in grids:
    sum_val += sum(row)

print(sum_val)