N = int(input())

# Write your code here!
def custom(cnt, n):
    if n == 1:
        return cnt

    if n % 2 != 0:
        return custom(cnt+1, n//3)
    else:
        return custom(cnt+1, n//2)

print(custom(0, N))