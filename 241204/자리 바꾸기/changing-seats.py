def count_sit(num):
    visited = [num]
    first = num
    count = 0
    i = 0
    while True:
        if input_list[i][0] == num:
            if num not in visited:
                visited.append(num)
            num = input_list[i][1]
            

        elif input_list[i][1] == num:
            if num not in visited:
                visited.append(num)
            num = input_list[i][0]
            

        i += 1
        if i == K:
            i = 0
            count += 1
        
        if (count >= 3 and first == num):
            break

    return len(visited)



N, K = map(int, input().split())
result = range(1, N+1)
input_list = []

for i in range(K):
    input_list.append(tuple(map(int, input().split())))

for i in range(1, N+1):
    print(count_sit(i))
