
import itertools
boardss=[]
n=int(input("n的值："))
list=[]
for i in range(n):
    list.append(str(i))
s="".join(list)
for nums in itertools.permutations(s,n):
    board=[["."] * n for i in range( n )]
    boards=[]
    for i in range(len(nums)):
        a=int(nums[i])
        flag=0
        for j in range(i+1,len(nums)):
            b=int(nums[j])
            if abs(a-b)==j-i:
                flag = 1
                break
        if flag==1:
            break
    if flag == 1:
        continue
    for i in range(n):
        board[i][int(nums[i])]="Q"
        boards.append("".join(board[i]))
    boardss.append(boards)
print(boardss)
