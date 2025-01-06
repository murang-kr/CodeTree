arr = list(map(int, input().split()))
max_val = arr[0]
min_val = arr[0]
for num in arr[1:]:
    if num == 999 or num == -999:
        break

    if num > max_val:
        max_val = num

    if num < min_val:
        min_val = num

print(max_val, min_val)