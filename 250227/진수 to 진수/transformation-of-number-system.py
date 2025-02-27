a, b = map(int, input().split())
n = input()

# Please write your code here.
num = 0
digits = []
for i in range(len(n)):
    num = num * a + int(n[i])

while True:
    if num < b:
        digits.append(num)
        break
    digits.append(num%b)
    num //= b

for n in digits[::-1]:
    print(n, end = "")