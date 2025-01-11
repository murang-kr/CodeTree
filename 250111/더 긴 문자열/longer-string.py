string1, string2 = input().split()
if len(string1) == len(string2):
    print("same")
else:
    longer = string1 if len(string1) > len(string2) else string2
    print(longer, len(longer))