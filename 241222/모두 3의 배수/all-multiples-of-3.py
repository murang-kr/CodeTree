flag = False
for i in range(5):
    n = int(input())
    if n % 3 != 0:
        flag = True
if flag:
    print("0")
else:
    print("1")