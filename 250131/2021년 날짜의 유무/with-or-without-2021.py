M, D = map(int, input().split())

# Write your code here!
def custom(m, d):
    if m > 12:
        return False

    if m == 2:
        if d <= 28:
            return True
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if d <= 31:
            return True
    else:
        if d <= 30:
            return True

    return False

if custom(M, D):
    print("Yes")
else:
    print("No")