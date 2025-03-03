N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
fines = [0 for _ in range(N+1)]
flag = True
for num in student:
    fines[num] += 1
    if fines[num] >= K: 
        print(num)
        flag = False
        break
if flag:
    print(-1)