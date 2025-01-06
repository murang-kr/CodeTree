n = int(input())
arr = list(map(int, input().split()))

distance = 99
for i in range(len(arr[:-1])):
    temp = arr[i+1] - arr[i]
    if temp < distance:
        distance = temp
print(distance)