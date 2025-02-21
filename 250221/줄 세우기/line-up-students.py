n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Write your code here!
students.sort(key=lambda x: (-x[0], -x[1], x[2]))

for height, weight, num in students:
    print(height, weight, num)