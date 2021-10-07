#模拟下棋
def chess(l,Q,n,board):
    a_copy_of_board=board.copy()
    if board[Q[0]][l] == ".":
        board[Q[0]][l]="Q"
    else:
        return chess(l+1,Q,n,board)
    for i in range(Q[0]+1,n):
        board[i][l]="X"
    for i in range(1,n-Q[0]):
        if l-i<0 and l+i>n-1:
            break
        if l-i>=0:
            board[Q[0]+i][l-i]="X"
        if l+i<=n-1:
            board[Q[0]+i][l+i]="X"
    if Q[0]<n-1:
        Q[0]=Q[0]+1
        l=0
    else:
        if "Q"in board[-1]:
            return board
    if "."in board[Q[0]]:
        return chess(l,Q,n,board)
    else:
        return []


n=4
boardss=[]
Q=[""]*n
for l in range(n):
    board = [["."] * n for i in range( n )]
    Q[0]=0
    board=chess( l, Q, n, board )
    if board==[]:
        continue
    boards=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]=="X":
                board[i][j]="."
    for i in range(n):
        boards.append("".join(board[i]))
    boardss.append(boards)
print(boardss)