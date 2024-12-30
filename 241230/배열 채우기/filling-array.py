temp = list(map(int, input().split()))
flag = False
for i in range(len(temp)):
    if temp[i] == 0:
        for item in temp[i-1::-1]:
            print(item, end = " ")
        flag = True
if not flag:
    for item in temp[::-1]:
            print(item, end = " ")