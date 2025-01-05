n, q = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
for _ in range(q):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        answer.append(arr[temp[1]-1])
    elif temp[0] == 2:
        flag = True
        for i, char in enumerate(arr):
            if temp[1] == char:
                answer.append(i+1)
                flag = False
                break
        if flag:
            answer.append(0)
    else:
        answer.append(" ".join(str(num) for num in arr[temp[1]-1:temp[2]]))

for item in answer:
    print(item)