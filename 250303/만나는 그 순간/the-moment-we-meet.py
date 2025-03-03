n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
p1_loc = [0]
p2_loc = [0]
flag = True

for i in range(n):
    dirc = 1
    if d[i] == "L": dirc = -1
    for j in range(t[i]):
        p1_loc.append(p1_loc[-1] + dirc)

for i in range(m):
    dirc = 1
    if d2[i] == "L": dirc = -1
    for j in range(t2[i]):
        p2_loc.append(p2_loc[-1] + dirc)

for i in range(1, min(len(p1_loc), len(p2_loc))):
    if p1_loc[i] == p2_loc[i]:
        print(i)
        flag = False
        break

if flag:
    print(-1)
