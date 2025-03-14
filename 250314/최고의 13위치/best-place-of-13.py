n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt_coin = 0
        cnt_coin += grid[i][j] + grid[i][j+1] + grid[i][j+2]
        cnt = max(cnt, cnt_coin)

print(cnt)