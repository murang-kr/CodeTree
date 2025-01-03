arr = list(map(int, input().split()))
for item in arr:
    if item == 0:
        break
    if item % 2 == 0:
        print(item//2, end = " ")
    else:
        print(item+3, end = " ")