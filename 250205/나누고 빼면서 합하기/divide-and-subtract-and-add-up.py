n, m = map(int, input().split())
A = list(map(int, input().split()))

# Write your code here!
def custom(num, arr):
    sum_val = 0
    while num >= 1:
        sum_val += arr[num-1]
        if num % 2 == 1:
            num -= 1
        else:
            num //= 2
    return sum_val

print(custom(m, A))