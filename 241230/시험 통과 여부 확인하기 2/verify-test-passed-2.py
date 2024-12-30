n = int(input())
grade = []
cnt = 0
for _ in range(n):
    temp = list(map(int, input().split()))
    average = sum(temp)/len(temp)
    if average >= 60:
        grade.append("pass")
    else:
        grade.append("fail")

for item in grade:
    print(item)
    if item == "pass":
        cnt += 1
print(cnt)