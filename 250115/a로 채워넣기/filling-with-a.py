s = input()
arr = list(s)
arr[1], arr[len(arr)-2] = "a", "a"
s = "".join(arr)
print(s)