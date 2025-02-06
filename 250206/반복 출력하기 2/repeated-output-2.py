n = int(input())

# Write your code here!
def print_s(n):
    if n == 0:
        return
    print_s(n-1)
    print("HelloWorld")

print_s(n)