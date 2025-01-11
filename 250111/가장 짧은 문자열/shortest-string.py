string_1 = input()
string_2 = input()
string_3 = input()

arr = sorted([string_1, string_2, string_3], key = lambda x: len(x))
print(len(arr[2])-len(arr[0]))