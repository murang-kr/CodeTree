a, b = map(int, input().split())
if a > b:
    big = a
    small = b
else:
    big = b
    small = a

for i in range(big, small-1, -1):
    print(i, end = " ")