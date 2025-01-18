A = input()
for i in range(len(A)):
    if A[i] == "e":
        A = A[:i] + A[i+1:]
        break

print(A)