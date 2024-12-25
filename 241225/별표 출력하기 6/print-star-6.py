n = int(input())
for i in range(n):
    for _ in range(i):
        print(" ", end = " ")
    for _ in range((2*(n-i))-1):
        print("*", end = " ")
    print()

for j in range(2, n+1):
    for _ in range(n-j):
        print(" ", end = " ")
    for _ in range((2*j)-1):
        print("*", end = " ")
    print()