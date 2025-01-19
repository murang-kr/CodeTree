A = input()
cmd = input()
for c in cmd:
    if c == "L":
        A = A[1:] + A[0]
        
    elif c == "R":
        A = A[len(A)-1] + A[:len(A)-1]
        
print(A)