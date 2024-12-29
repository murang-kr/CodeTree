start, end = map(int, input().split())
cnt = 0
for i in range(start, end+1):
    temp = []
    for j in range(1, i):
        if i % j == 0:
            temp.append(j)
    if i == sum(temp):
        cnt += 1
print(cnt)