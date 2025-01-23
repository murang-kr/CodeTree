n, m = map(int, input().split())

# Write your code here!
def find_maximum_common_divisor(n, m):
    if n == m:
        print(n)
        return

    divisor = n if n > m else m
    for _ in range(divisor):
        if n % divisor == 0 and m % divisor == 0:
            print(divisor)
            return
        else:
            divisor -= 1

find_maximum_common_divisor(n, m)