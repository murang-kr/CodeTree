n = int(input())
temp = []
for i in range(n):
    a, b = map(int, input().split())
    sum_val = 0
    for j in range(a, b+1):
        if j % 2 == 0:
            sum_val += j
    temp.append(sum_val)
for item in temp:
    print(item)