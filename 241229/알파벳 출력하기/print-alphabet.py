n = int(input())
a = ord('A')
for i in range(1, n+1):
    for j in range(i):
        print(chr(a), end = "")
        a += 1
    print()