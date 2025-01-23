n = int(input())

# Write your code here!
def make_square(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num, end = " ")
            num += 1
            if num >= 10:
                num = 1
        print()

make_square(n)