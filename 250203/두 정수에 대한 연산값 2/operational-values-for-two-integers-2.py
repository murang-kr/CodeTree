a, b = map(int, input().split())

# Write your code here!
def custom(a, b):
    if a == max(a, b):
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a, b

r1, r2 = custom(a, b)
print(r1, r2)