temp = list(map(int, input().split()))
for i in range(len(temp)):
    if temp[i] == 0:
        print(temp[i-1]+temp[i-2]+temp[i-3])
        break