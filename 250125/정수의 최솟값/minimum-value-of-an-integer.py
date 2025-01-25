a, b, c = map(int, input().split())

# Write your code here!
def custom(*args):
    return min(args)

print(custom(a, b, c))