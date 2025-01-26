a, b = map(int, input().split())

# Write your code here!
def check_decimal(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum_val = 0
for i in range(a, b+1):
    if check_decimal(i):
        sum_val += i

print(sum_val)