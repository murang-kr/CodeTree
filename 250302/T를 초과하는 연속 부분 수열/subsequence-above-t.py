n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
max_cnt = 0
for i in range(len(arr)):
    if arr[i] <= t:
        continue
        
    if i == 0 or (arr[i] > t and arr[i-1] > t):
        cnt += 1
    else:
        cnt = 1
        
    if cnt > max_cnt:
            max_cnt = cnt

print(max_cnt)