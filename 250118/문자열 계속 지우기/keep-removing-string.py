A = input()
B = input()

# Write your code here!
while True:
    if B in A:
        A = A.replace(B, "")
    else:
        break

print(A)