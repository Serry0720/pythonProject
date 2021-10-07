# 模拟下棋
def chess(l, h, n, board):
    a_copy_of_board = board.copy()
    if board[h][l] == ".":
        board[h][l] = "Q"
    else:
        return chess( l + 1, h, n, board )
    for i in range( h + 1, n ):
        board[i][l] = "X"
    for i in range( 1, n - h ):
        if l - i < 0 and l + i > n - 1:
            break
        if l - i >= 0:
            board[h + i][l - i] = "X"
        if l + i <= n - 1:
            board[h + i][l + i] = "X"
    if h < n - 1:
        h = h + 1
        l = 0
    else:
        if "Q" in board[-1]:
            return board
    if "." in board[h]:
        return chess( l, h, n, board )
    else:

        return chess( l, h, n, board )


n = int( input( "n的大小:" ) )
boardss = []
Q = [""] * n
for l in range( n ):
    board = [["."] * n for i in range( n )]
    h = 0
    board = chess( l, h, n, board )
    if board == []:
        continue
    boards = []
    for i in range( n ):
        for j in range( n ):
            if board[i][j] == "X":
                board[i][j] = "."
    for i in range( n ):
        boards.append( "".join( board[i] ) )
    boardss.append( boards )
print( boardss )
