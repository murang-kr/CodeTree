n = int(input())
sum_val = 0
for i in range(1, 101):
    if sum_val + i >= n:
        break
    sum_val += i

if sum_val == 0:
    sum_val += n

print(sum_val)