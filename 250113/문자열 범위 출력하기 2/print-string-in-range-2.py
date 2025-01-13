string = input()
num = int(input())
if num > len(string):
    num = len(string)
for i in range(1, num+1):
    print(string[-i], end = "")