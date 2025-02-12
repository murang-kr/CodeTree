N = int(input())

# Write your code here!
def custom(n):
    if n < 10:
        return n**2
    return custom(n//10)+((n%10)**2)

print(custom(N))