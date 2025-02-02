A = input()

# Write your code here!
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

if is_palindrome(A):
    print("Yes")
else:
    print("No")