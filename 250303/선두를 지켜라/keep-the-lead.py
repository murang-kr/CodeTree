n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
cnt = 0
a_loc, b_loc = [0], [0]
head = None

for i in range(n):
    vec = v[i]
    for j in range(t[i]):
        a_loc.append(a_loc[-1] + vec)

for i in range(m):
    vec = v2[i]
    for j in range(t2[i]):
        b_loc.append(b_loc[-1] + vec)

for i in range(1, len(a_loc)):
    if a_loc[i] == b_loc[i]: continue

    if a_loc[i] > b_loc[i]:
        if head != "A":
            cnt += 1
            head = "A"
    else:
        if head != "B":
            cnt += 1
            head = "B"

    
print(cnt-1)