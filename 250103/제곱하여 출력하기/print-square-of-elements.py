n = int(input())
temp = list(map(int, input().split()))
solve = [item**2 for item in temp]
for item in solve:
    print(item, end = " ")