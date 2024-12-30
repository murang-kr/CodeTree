temp = list(map(int, input().split()))
cnt = 0
sum_val = 0
for item in temp:
    if item == 0:
        break
    elif item % 2 == 0:
        sum_val += item
        cnt += 1
print(cnt, sum_val)