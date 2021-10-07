q = []
def perm(n ,begin , end):#使用递归进行全排列
  global q#将q定义成全局变量
  if begin == end:#判断是否排序到最后一个数
    q += n
  else:
    i = begin
    for num in range(begin , end):
      n[num], n[i] = n[i], n[num]
      perm(n, begin + 1, end)
      n[num], n[i] = n[i], n[num]
n = int(input())#输入整数n
a = []
for i in range(1, n+1):#获取1~n的列表
  a.append(i)
perm(a , 0 , n)
b = []
temp = 1
for w in range(1 , n+1):#获得输出行数
  temp *= w
for j in range(0 , temp):#将perm中q所得的列表进行拆分
  b.append(q[j*n:j*n+n])
ss = sorted(b)#排序
for r in ss:
  for c in r:
    print(c , end=' ')
  print()