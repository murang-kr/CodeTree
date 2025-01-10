n = int(input())
arr = [[1 for _ in range(i+1)] for i in range(n)]
if n > 2:
    for i in range(2, n):
        for j in range(i):
            if j != 0 and j != i:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()