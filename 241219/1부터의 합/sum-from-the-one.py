n = int(input())
sum_val = 0
pre = 0
for i in range(1, 101):
    if sum_val >= n:
        break
    pre = sum_val
    sum_val += i
print(pre)