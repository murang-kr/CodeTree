n = int(input())
temp = list(map(int, input().split()))
for item in temp[::-1]:
    if item % 2 == 0:
        print(item, end = " ")