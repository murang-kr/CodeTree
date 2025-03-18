n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
import sys
distance = sys.maxsize
for i in range(n):
    route = a[i:] + a[:i]
    dis = 0
    for j in range(len(route)):
        dis += route[j] * j
    distance = min(dis, distance)
print(distance)