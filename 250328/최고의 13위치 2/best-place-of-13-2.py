n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_cnt = 0
for i in range(n):
    for j in range(n - 2):
        for k in range(i+1, n):
            for l in range(n - 2):
                max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1] + arr[i][j+2]
                                     + arr[k][l] + arr[k][l + 1] + arr[k][l+2])

if n > 6:
    for i in range(n-5):
        max_cnt = max(max_cnt, arr[n-1][i] + arr[n-1][i+1] + arr[n-1][i+2]
                                + arr[n-1][i+3] + arr[n-1][i+4] + arr[n-1][i+5])

print(max_cnt)