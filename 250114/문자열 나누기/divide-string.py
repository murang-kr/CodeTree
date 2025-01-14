n = int(input())
arr = list(input().split())
answer = "".join(arr)
cnt = 0
for char in answer:
    print(char, end = "")
    cnt += 1
    if cnt == 5:
        print()
        cnt = 0
