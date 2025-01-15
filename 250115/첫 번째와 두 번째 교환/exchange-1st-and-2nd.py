s = input()
arr = list(s)
c1, c2 = arr[0], arr[1]
for i in range(len(arr)):
    if arr[i] == c1:
        arr[i] = c2
    elif arr[i] == c2:
        arr[i] = c1
s = "".join(arr)
print(s)