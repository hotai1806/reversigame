board = [['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', 'W', 'B', '.', '.', '.'],
['.', '.', '.', 'B', 'W', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.']]

HEIGHT = 8
WIDTH = 8
board = []
def PrintBoard(board):

    for i in range(WIDTH):
        board.append(['.', '.', '.', '.', '.', '.', '.', '.'])

    print(" a b c d e f g h")
    for y in range(HEIGHT):
        print('%s' % (y + 1), end = ' ')
        for x in range(WIDTH):
            print(board[x][y], end= ' ')
        print()
        board[3][3] = "W"
        board[3][4] = "B"
        board[4][3] = "B"
        board[4][4] = "W"

def isOnBoard(x,y):
    return x >= 0 and x < 7 and y >= 0 and y <= 7

def player1(0):
    go0 = 'a b c d e f g h'.split()
    go1 = '1 2 3 4 5 6 7 8'.split()
    while True:
        move = input().lower()
        pass


def player2(0):
    pass
def Availablemove(board,tile,xs,ys):
    if board[xs][ys] != " " or not isOnBoard(xs,ys):
        return False

    board[xs][ys] = tile
    if tile == "B"
        otherTile = "W"
    else:
        otherTile = "B"
    tilesToFlip = []
    tx =[[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for xs, ys in tx:
        x, y = xs, xy
        x + = xdirection
        y + = ydirection
        if not isOnBoard(x,y)
            continue
        while board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True
                    x -= xdirection
                 tilesToFlip.append([x, y])

    board[xs][ys] = '.'
    if len(tilesToFlip) == 0:
        return print()
    return tilesToFlip
