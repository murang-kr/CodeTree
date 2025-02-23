n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Write your code here!
students = []
for i in range(n):
    students.append((name[i], height[i], weight[i]))

students.sort(key = lambda x: (x[1], -x[2]))

for name, hei, wei in students:
    print(name, hei, wei)
