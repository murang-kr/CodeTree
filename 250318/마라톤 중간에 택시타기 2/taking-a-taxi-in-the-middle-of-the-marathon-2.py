n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys
min_distance = sys.maxsize

for i in range(1, len(points)-1):
    without_point = points[:i] + points[i+1:]
    distance = 0
    for i in range(1, len(without_point)):
        distance += abs(without_point[i-1][0]-without_point[i][0])+abs(without_point[i-1][1]-without_point[i][1])
    min_distance = min(min_distance, distance)

print(min_distance)