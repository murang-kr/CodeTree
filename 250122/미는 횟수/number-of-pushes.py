A = input()
B = input()

for i in range(len(A)):
    A = A[len(A)-1]+A[:len(A)-1]
    if A == B:
        print(i+1)
        break
    elif i == len(A)-1:
        print(-1)
