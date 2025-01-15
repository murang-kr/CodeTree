s, q = input().split()
s = list(s)

for i in range(int(q)):
    cmd1, cmd2, cmd3 = input().split()
    if int(cmd1) == 1:
        idx1, idx2 = int(cmd2)-1, int(cmd3)-1
        s[idx1], s[idx2] = s[idx2], s[idx1]
        print("".join(s))
    else:
        for i in range(len(s)):
            if s[i] == cmd2:
                s[i] = cmd3
        print("".join(s))