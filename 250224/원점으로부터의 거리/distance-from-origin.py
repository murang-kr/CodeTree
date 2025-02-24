n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Write your code here!
points.sort(key = lambda x: abs(x[1][0]) + abs(x[1][1]))
for idx, point in points:
    print(idx+1)