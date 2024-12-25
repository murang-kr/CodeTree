n = int(input())
for i in range(2*n):
    if i % 2 == 1:
        for _ in range(int(1+(i-1)/2)):
            print("*", end = " ")
        print()
    else:
        for _ in range(int(n-(i/2))):
            print("*", end = " ")
        print()