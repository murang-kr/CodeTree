n = int(input())
temp = []
for i in range(2, n+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False

    if flag:
        temp.append(i)

for item in temp:
    print(item, end = " ")