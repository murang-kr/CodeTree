a = input()
b = input()

possible_a = []
for i in range(len(a)):
    if a[i] == "1":
        temp = a[:i] + "0" + a[i + 1:]
        possible_a.append(temp)
    else:
        temp = a[:i] + "1" + a[i + 1:]
        possible_a.append(temp)

possible_b = []
for i in range(len(b)):
    if b[i] == "0":
        temp1 = b[:i] + "1" + b[i + 1:]
        possible_b.append(temp1)

        temp2 = b[:i] + "2" + b[i + 1:]
        possible_b.append(temp2)

    elif b[i] == "1":
        temp1 = b[:i] + "0" + b[i + 1:]
        possible_b.append(temp1)

        temp2 = b[:i] + "2" + b[i + 1:]
        possible_b.append(temp2)

    else:
        temp1 = b[:i] + "0" + b[i + 1:]
        possible_b.append(temp1)

        temp2 = b[:i] + "1" + b[i + 1:]
        possible_b.append(temp2)

a_list = [int(_, 2) for _ in possible_a]
b_list = [int(_, 3) for _ in possible_b]

result = list(set(a_list) & set(b_list))
print(result[0])