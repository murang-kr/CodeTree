n = int(input())
temp = []
for i in range(n):
    cnt = 0
    val = int(input())

    while val != 1:
        if val % 2 == 1:
            val *= 3
            val += 1
        else:
            val //= 2
        cnt += 1
        
    temp.append(cnt)

for i in range(len(temp)):
    print(temp[i])