first_cold, first_temp = input().split()
second_cold, second_temp = input().split()
third_cold, third_temp = input().split()

patient = [(first_cold, first_temp), (second_cold, second_temp), (third_cold, third_temp)]
result = []

for item in patient:
    if item[0] == "Y" and int(item[1]) >= 37:
        result.append("A")
    elif item[0] == "N" and int(item[1]) >= 37:
        result.append("B")
    elif item[0] == "Y" and int(item[1]) < 37:
        result.append("C")
    else:
        result.append("D")

count = 0

for item in result:
    if item == "A":
        count += 1

if count >= 2:
    print("E")
else:
    print("N")