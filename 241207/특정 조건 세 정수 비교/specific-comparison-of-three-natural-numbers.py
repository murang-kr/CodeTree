temp = list(map(int, input().split()))
if temp[0] == min(temp):
    print("1", end = " ")
else:
    print("0", end = " ")

if len(set(temp)) == 1:
    print("1", end = " ")
else:
    print("0", end = " ")