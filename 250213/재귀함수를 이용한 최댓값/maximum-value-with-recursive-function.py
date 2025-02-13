n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def f(n, max_val):
    global arr
    if n == 0:
        return max_val

    if arr[n-1] > max_val:
        return f(n-1, arr[n-1])
    else:
         return f(n-1, max_val)

print(f(n, 0))