n = int(input())
sum_val = 0
for i in range(1, 101):
    if sum_val + i >= n:
        break
    sum_val += i
print(sum_val)