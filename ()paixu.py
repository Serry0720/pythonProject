s="()"
list=[]
for i in s:
    if i=="("or i=="["or i=="{":
        list.append(i)
    elif i==")":
        if list[-1]=="(":
            list.pop()
        else:
            break
    elif i=="]":
        if list[-1]=="[":
            list.pop()
        else:
            break
    elif i=="}":
        if list[-1]=="{":
            list.pop()
        else:
            break
if list == []:
    print ("ture")
else:
    print ("false")
