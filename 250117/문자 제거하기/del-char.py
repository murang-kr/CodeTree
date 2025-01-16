arr = list(input())
idx = []
for _ in range(len(arr)-1):
    i = int(input())
    idx.append(i)

for i in idx:
    if i >= len(arr):
        arr.pop(-1)
    else:
        arr.pop(i)
    print("".join(arr))