n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
blocks = [0] * 2001
spawn = 1000

for i in range(n):
    if dir[i] == "R":
        for j in range(spawn, spawn+x[i]):
            blocks[j] += 1
        spawn += x[i]
    else:
        for j in range(spawn-x[i], spawn):
            blocks[j] += 1
        spawn -= x[i]

sum_val = 0
for num in blocks:
    if num >= 2:
        sum_val += 1

print(sum_val)