n = int(input())
temp = list(map(int, input().split()))
new = []
for item in temp:
    if item % 2 == 0:
        new.append(item)

for item in new:
    print(item, end = " ")