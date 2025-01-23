n, m = map(int, input().split())

# Write your code here!
def find_minimum_common_multiple(n, m):
    if n == m:
        print(n)
        return

    multiple = n if n > m else m
    while True:
        if multiple % n == 0 and multiple % m == 0:
            print(multiple)
            return
        else:
            multiple += 1

find_minimum_common_multiple(n, m)