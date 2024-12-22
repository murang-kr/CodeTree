a, b, c = map(int, input().split())
flag = False
for i in range(a,b+1):
    if i % c == 0:
        flag = True
    if flag:
        break
if flag:
    print("YES")
else:
    print("NO")