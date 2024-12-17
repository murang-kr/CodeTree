n = int(input())
sum_val = 0
for _ in range(n):
    temp = int(input())
    sum_val += temp
average = sum_val / n
print(sum_val, f"{average:.1f}")