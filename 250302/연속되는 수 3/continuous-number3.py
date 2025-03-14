N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
cnt = 0
max_cnt = 0
for i in range(len(arr)):
    if i == 0 or arr[i] * arr[i-1] > 0:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    else:
        cnt = 1

print(max_cnt)