n = int(input())
flag = False
for i in range(2, n):
    if n % i == 0:
        flag = True
        break
if flag:
    print("C")
else:
    print("P")