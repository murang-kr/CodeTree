A = input()

# Write your code here!
def custom(s):
    for i in range(1, len(s)):
        if s[0] != s[i]:
            return True
    return False

if custom(A):
    print("Yes")
else:
    print("No")