arr = list(map(int, input().split()))
max_val = arr[0]
for num in arr:
    if num > max_val:
        max_val = num

print(max_val)