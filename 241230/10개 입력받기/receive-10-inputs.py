temp = list(map(int, input().split()))
flag = False
for i in range(len(temp)):
    if temp[i] == 0:
        print(sum(temp[:i:]), f"{sum(temp[:i:])/i:.1f}")
        flag = True
        break
if not flag:
    print(sum(temp), f"{sum(temp)/len(temp):.1f}")