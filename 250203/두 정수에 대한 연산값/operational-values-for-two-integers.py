a, b = map(int, input().split())

# Write your code here!
def custom(a, b):
    if a == max(a, b):
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    return a, b 

r1, r2 = custom(a, b)
print(r1, r2)