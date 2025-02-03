n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def custom(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] *= -1

custom(arr)
for elem in arr:
    print(elem, end = " ")