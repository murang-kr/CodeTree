n = int(input())
cnt = 0
for i in range(n):
    if i % 2 == 0:
        for _ in range(n):
            cnt += 1
            print(cnt, end = " ")
    else:
        for _ in range(n):
            cnt += 2
            print(cnt, end = " ")
    print()