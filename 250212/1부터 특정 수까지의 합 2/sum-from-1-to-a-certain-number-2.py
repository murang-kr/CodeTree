N = int(input())

# Write your code here!
def custom(n):
    if n == 1:
        return 1
    return custom(n-1) + n

print(custom(N))