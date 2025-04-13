N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 9999
for i in range(N-T+1):
    temp = arr[i:i+T]
    cost = 0
    for elem in temp:
        cost += abs(H - elem)
    cnt = min(cnt, cost)

print(cnt)