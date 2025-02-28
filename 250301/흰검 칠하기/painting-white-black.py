n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
blocks = [0] * 200001
blacks = [0] * 200001
whites = [0] * 200001
spawn = 100000

for i in range(n):
    if dir[i] == "R":
        dis = x[i]
        while dis > 0:
            blocks[spawn] = "B"
            blacks[spawn] += 1
            dis -= 1
            if dis:
                spawn += 1
    else:
        dis = x[i]
        while dis > 0:
            blocks[spawn] = "W"
            whites[spawn] += 1
            dis -= 1
            if dis:
                spawn -= 1

cnt_color = [0, 0, 0]
for i in range(len(blocks)):
    if blocks[i] != 0:
        if whites[i] >= 2 and blacks[i] >= 2:
            cnt_color[2] += 1
        else:
            if blocks[i] == "W":
                cnt_color[0] += 1
            else:
                cnt_color[1] += 1


for num in cnt_color:
    print(num, end = " ")