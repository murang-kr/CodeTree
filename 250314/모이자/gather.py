n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
import sys
min_move = sys.maxsize

for i in range(n):
    move = 0
    for j in range(n):
        move += abs(i-j) * A[j]
    min_move = min(min_move, move)

print(min_move)