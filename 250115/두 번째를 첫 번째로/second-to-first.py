arr = list(input())

c1, c2 = arr[0], arr[1]
for i in range(len(arr)):
    if arr[i] == c2:
        arr[i] = c1

print("".join(arr))