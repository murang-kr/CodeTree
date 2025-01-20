c1, c2 = input().split()

if ord(c1) > ord(c2):
    print(ord(c1)+ord(c2), ord(c1)-ord(c2))
else:
    print(ord(c1)+ord(c2), ord(c2)-ord(c1))