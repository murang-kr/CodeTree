s1 = input()
s2 = input()
num1, num2 = "", ""
for c in s1:
    if c.isdigit():
        num1 += c

for c in s2:
    if c.isdigit():
        num2 += c

print(int(num1)+int(num2))