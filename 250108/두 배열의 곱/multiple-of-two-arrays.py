arr_1, arr_2 = [], []
for _ in range(3):
    a = list(map(int, input().split()))
    arr_1.append(a)

temp = input()

for _ in range(3):
    a = list(map(int, input().split()))
    arr_2.append(a)

for i in range(3):
    for j in range(3):
        print(arr_1[i][j]*arr_2[i][j], end = " ")
    print()