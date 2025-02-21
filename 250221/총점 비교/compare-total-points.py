n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Write your code here!
students = []
for i in range(n):
    students.append((name[i], score1[i], score2[i], score3[i]))

students.sort(key = lambda x: (x[1]+x[2]+x[3]))
for name, sc1, sc2, sc3 in students:
    print(name, sc1, sc2, sc3)