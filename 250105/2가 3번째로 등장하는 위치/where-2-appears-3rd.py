n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i, c in enumerate(arr):
    if c == 2:
        if cnt == 2:
            print(i+1)
            break
        else:
            cnt += 1