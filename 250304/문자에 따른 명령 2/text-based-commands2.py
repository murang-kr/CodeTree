dirs = input()

# Please write your code here.
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direction = 3
cur_loc = (0, 0)
# rotate direction
for direct in dirs:
    if direct == "L":
        direction = (direction + 3) % 4
    elif direct == "R":
        direction = (direction + 1) % 4
    else:
        cur_loc = (cur_loc[0]+dx[direction], cur_loc[1]+dy[direction])

print(cur_loc[0], cur_loc[1])