temp = list(map(int, input().split()))
sum_val = 0
cnt = 0
for item in temp:
    if item >= 250:
        break
    else:
        sum_val += item
        cnt += 1

print(sum_val, f"{sum_val/cnt:.1f}")