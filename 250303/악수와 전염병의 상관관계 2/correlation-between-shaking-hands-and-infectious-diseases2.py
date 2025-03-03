N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
diseased = [0 for _ in range(N+1)]
contagious_people = [0 for _ in range(N+1)]
diseased[P], contagious_people[P] = 1, K
handshakes.sort(key = lambda x: x[0])

for t, x, y in handshakes:
    if contagious_people[x] >= 1:
        contagious_people[x] -= 1
        if diseased[y] != 1:
            diseased[y] = 1
            contagious_people[y] = K
            continue

    if contagious_people[y] >= 1:
        contagious_people[y] -= 1
        if diseased[x] != 1:
            diseased[x] = 1
            contagious_people[x] = K

for num in diseased[1:]:
    print(num, end = "")