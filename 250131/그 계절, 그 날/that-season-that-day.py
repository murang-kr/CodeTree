Y, M, D = map(int, input().split())

# Write your code here!
def is_leap_year(n):
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        return True
    else:
        return False

def is_exist_day(y, m, d):
    if m == 2:
        if is_leap_year(y):
            if d <= 29:
                return True
        else:
            if d <= 28:
                return True
        return False
        
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        if d != 31:
            return True

    return False

if is_exist_day(Y, M, D):
    if M >= 3 and M <= 5:
        print("Spring")
    elif M >= 6 and M <= 8:
        print("Summer")
    elif M >= 9 and M <= 11:
        print("Fall")
    else:
        print("Winter")
else:
    print("-1")