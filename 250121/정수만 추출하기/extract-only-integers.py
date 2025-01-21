a, b = input().split()
num1, num2 = "", ""
for c in a:
    if not c.isdigit():
        break
    else:
        num1 += c

for c in b:
    if not c.isdigit():
        break
    else:
        num2 += c

print(int(num1)+int(num2))