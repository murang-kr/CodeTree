N = int(input())

# Write your code here!
def f(n):
    if n == 1:
        return 1
    return f(n-1) * n

print(f(N))