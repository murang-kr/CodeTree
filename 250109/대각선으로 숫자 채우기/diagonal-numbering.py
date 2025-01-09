n, m = map(int, input().split())

# Write your code here!
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for i in range(n+m-1):
    r, c = 0, i
    if i >= m:
        r = i-m+1
        c = m-1
    while True:
        arr[r][c] = num
        num += 1
        if r == n-1 or c == 0:
            break
        else:
            r += 1
            c -= 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()