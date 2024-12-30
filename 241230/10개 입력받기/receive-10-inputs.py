temp = list(map(int, input().split()))
flag = False
for i in range(len(temp)):
    if temp[i] == 0:
        print(sum(temp[:i:]), sum(temp[:i:])/i)
        flag = True
        break
if not flag:
    print(sum(temp), sum(temp)/len(temp))