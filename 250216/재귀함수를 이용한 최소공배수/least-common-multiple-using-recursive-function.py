n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    
def lcm(a, b):
    return a * b // gcd(a, b)

def f(arr):
    if len(arr) == 1:
        return arr[0]
    return lcm(arr[0], f(arr[1:]))

print(f(arr))