N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
candy = [0] * 100

# Please write your code here.
max_candy = 0
for c, p in arr:
    candy[p-1] += c

for i in range(100):
    temp = candy[i-K:i+K+1]
    max_candy = max(max_candy, sum(temp))

print(max_candy)