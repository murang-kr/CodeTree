n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
max_score = 0
arr = [0]*max(x)
for i in range(n):
    arr[x[i]-1] = c[i]

for i in range(len(arr)-k):
    sum_score = 0
    for j in range(k+1):
        if arr[i+j] == "G": sum_score += 1
        elif arr[i+j] == "H": sum_score += 2
    max_score = max(max_score, sum_score)

print(max_score)