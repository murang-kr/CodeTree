a, b = map(int, input().split())

# Write your code here!
import math
def custom(n):
    if n <= 1:
        return False
    if n == 2:
        if sum_is_even(n):
            return True
        else:
            return False
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    if sum_is_even(n):
        return True
    else:
        return False

def sum_is_even(n):
    sum_val = 0
    n = str(n)
    for num in n:
        sum_val += int(num)
    if sum_val % 2 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    if custom(i):
        cnt += 1
    
print(cnt)