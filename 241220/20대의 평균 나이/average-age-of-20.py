sum_val = 0
cnt = 0
while True:
    n = int(input())
    if n // 10 != 2:
        break
    sum_val += n
    cnt += 1
average = sum_val / cnt
print(f"{average:.2f}")