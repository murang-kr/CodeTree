n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
arr2 = []
for i in range(n):
    arr2.append(arr[i])
    if i % 2 == 0:
        arr2.sort()
        print(arr2[len(arr2)//2], end = " ")