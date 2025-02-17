n = int(input())
arr = [input() for _ in range(n)]

arr.sort()

for item in arr:
    print(item)