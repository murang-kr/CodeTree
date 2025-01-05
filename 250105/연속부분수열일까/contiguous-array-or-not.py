n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(len(A)):
    if len(B) > len(A)-i or len(A)-i == 1:
        print("No")
        break

    if A[i] == B[0]:
        if A[i:i+len(B)] == B:
            print("Yes")
            break
