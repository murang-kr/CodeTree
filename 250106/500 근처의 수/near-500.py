arr = list(map(int, input().split()))
up_val, down_val = 1000, 1
for num in arr:
    if num > 500 and num < up_val:
        up_val = num
    elif num < 500 and num > down_val:
        down_val = num

print(down_val, up_val)