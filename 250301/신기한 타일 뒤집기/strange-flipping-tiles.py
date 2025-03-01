n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
blocks = [0] * 200001
spawn = 100000

for i in range(n):
    if dir[i] == "R":
        dis = x[i]
        while dis > 0:
            blocks[spawn] = "B"
            dis -= 1
            if dis:
                spawn += 1
    else:
        dis = x[i]
        while dis > 0:
            blocks[spawn] = "W"
            dis -= 1
            if dis:
                spawn -= 1

cnt_color = [0, 0]
for i in range(len(blocks)):
    if blocks[i] != 0:
        if blocks[i] == "W":
            cnt_color[0] += 1
        else:
            cnt_color[1] += 1

print(cnt_color[0], cnt_color[1])