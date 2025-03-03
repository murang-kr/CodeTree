n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
a_loc, b_loc = [0], [0]
cnt = 0
before_meet = True

for i in range(n):
    dirc = 1
    if d[i] == "L": dirc = -1
    for j in range(t[i]):
        a_loc.append(a_loc[-1] + dirc)

for i in range(m):
    dirc = 1
    if d_b[i] == "L": dirc = -1
    for j in range(t_b[i]):
        b_loc.append(b_loc[-1] + dirc)

for i in range(1, min(len(a_loc), len(b_loc))):
    if a_loc[i] == b_loc[i]:
        if not before_meet:
            before_meet = True
            cnt += 1
    else:
        before_meet = False

if len(a_loc) != len(b_loc):
    remaining_robot = None
    if len(a_loc) > len(b_loc):
        remaining_robot, another = a_loc, b_loc
    else:
        remaining_robot, another = b_loc, a_loc

    for i in range(min(len(a_loc), len(b_loc)), max(len(a_loc), len(b_loc))):
        if remaining_robot[i] == another[-1]:
            if not before_meet:
                before_meet = True
                cnt += 1
        else:
            before_meet = False
print(cnt)