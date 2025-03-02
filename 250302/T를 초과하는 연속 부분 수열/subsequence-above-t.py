n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
max_cnt = 0
for i in range(len(arr)):
    if i == 0 or (arr[i] > arr[i-1] and arr[i] > t and arr[i-1] > t):
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1
if max_cnt == 1:
    print(0)
else:
    print(max_cnt)