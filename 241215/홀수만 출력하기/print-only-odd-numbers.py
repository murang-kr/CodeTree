N = int(input())
temp = []
for _ in range(N):
    temp.append(int(input()))

for item in temp:
    if item % 3 == 0 and item % 2 == 1:
        print(item)