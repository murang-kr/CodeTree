n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

arr.sort(key = lambda x: (x[1], x[2], x[3]), reverse = True)
for name, kor, eng, math in arr:
    print(name, kor, eng, math)
