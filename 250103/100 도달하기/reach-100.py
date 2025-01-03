n = int(input())
pp, p = 1, n
print(pp, p, end = " ")
while True:
    pp, p = p, pp+p
    print(p, end = " ")
    if p > 100:
        break