N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
cnt = 0
a_loc, b_loc = [0], [0]
the_hall_of_fame = [0]

for i in range(N):
    vec = v[i]
    for j in range(t[i]):
        a_loc.append(a_loc[-1] + vec)

for i in range(M):
    vec = v2[i]
    for j in range(t2[i]):
        b_loc.append(b_loc[-1] + vec)

for i in range(1, len(a_loc)):
    combi = None
    if a_loc[i] == b_loc[i]:
        combi = "AB"
    elif a_loc[i] > b_loc[i]:
        combi = "A"
    else:
        combi = "B"
    the_hall_of_fame.append(combi)
    
for i in range(1, len(the_hall_of_fame)):
    if the_hall_of_fame[i] != the_hall_of_fame[i-1]:
        cnt += 1
print(cnt)