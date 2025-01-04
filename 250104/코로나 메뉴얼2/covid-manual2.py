result = [0]*4
for _ in range(3):
    cold, temp = input().split()
    if cold == "Y" and int(temp) >= 37:
        result[0] += 1
    elif cold == "N" and int(temp) >= 37:
        result[1] += 1
    elif cold == "Y" and int(temp) < 37:
        result[2] += 1
    else:
        result[3] += 1

for item in result:
    print(item, end = " ")
if result[0] >= 2:
    print("E")