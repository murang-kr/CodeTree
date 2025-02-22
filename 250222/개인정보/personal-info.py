n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Write your code here!
students = []
for i in range(5):
    students.append((name[i], height[i], weight[i]))

students.sort(key = lambda x: x[0])

print("name")
for name, hei, wei in students:
    print(name, hei, wei)

print()
students.sort(key = lambda x: -x[1])
print("height")
for name, hei, wei in students:
    print(name, hei, wei)