n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i, n):
        avg = sum(arr[i:j+1]) / len(arr[i:j+1])
        if avg in arr[i:j+1]: cnt += 1
       
print(cnt)