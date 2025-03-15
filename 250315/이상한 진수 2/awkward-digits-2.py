a = list(input())

# Please write your code here.
flag = True
for i in range(len(a)):
    if a[i] == "0":
        a[i] = "1"
        flag = False
        break

if flag:
    a[-1] = "0"
    a = "".join(a)
    print(int(a, 2))
else:
    a = "".join(a)
    print(int(a, 2))