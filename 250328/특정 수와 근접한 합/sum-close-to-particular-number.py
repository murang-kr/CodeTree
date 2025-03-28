N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
difference = 9999
for i in range(N):
    for j in range(i+1, N):
        sum_val = sum(arr[:i]) + sum(arr[i+1:j]) + sum(arr[j+1:])
        difference = min(difference, abs(sum_val-S))
print(difference)