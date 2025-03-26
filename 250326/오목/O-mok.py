board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
def in_board(x, y):
    return 0 <= x and 0 <= y and x <= 18 and y <= 18

def check(x, y):
    baduk = board[x][y]
    cnt_1 = 0
    cnt_2 = 0
    if in_board(x, y+4):
        if len(set([baduk, board[x][y+1], board[x][y+2], board[x][y+3], board[x][y+4]])) == 1:
            return x, y+2

    if in_board(x+4, y):
        if len(set([baduk, board[x+1][y], board[x+2][y], board[x+3][y], board[x+4][y]])) == 1:
            return x+2, y

    if in_board(x, y+4) and in_board(x+4, y):
        if len(set([baduk, board[x+1][y+1], board[x+2][y+2], board[x+3][y+3], board[x+4][y+4]])) == 1:
            return x+2, y+2
    return -1, -1

flag = True
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            x, y = check(i, j)
            if x >= 0 and y >= 0:
                print(board[i][j])
                print(x+1, y+1)
                flag = False

if flag:
    print(0)