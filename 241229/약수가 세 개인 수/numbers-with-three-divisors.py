start, end = map(int, input().split())
cnt = 0
for i in range(start, end+1):
    temp = []
    for j in range(1, i+1):
        if i % j == 0:
            temp.append(j)
    if len(temp) == 3:
        cnt += 1
print(cnt)