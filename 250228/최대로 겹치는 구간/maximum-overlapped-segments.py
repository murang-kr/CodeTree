n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
blocks = [0] * 200
offset = 100
for a, b in segments:
    for i in range(a+offset, b+offset):
        blocks[i] += 1

print(max(blocks))