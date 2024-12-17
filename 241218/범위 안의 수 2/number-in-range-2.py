sum_val = 0
cnt = 0
for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        sum_val += n
        cnt += 1

average = sum_val / cnt
print(sum_val, f"{average:.1f}")
