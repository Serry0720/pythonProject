import turtle as t
import time
tim=time.strftime('%Y%m%d',time.gmtime())
t.setup(1700,400)
t.penup()
t.fd(-750)
t.pensize(3)
for i in range(8):
    ti=eval(tim[i])
    if ti in [2,3,4,5,6,8,9]:#中
        t.pendown()
    t.fd(-100)
    if ti in [0, 4, 5, 6, 8, 9]:#左上
        t.pendown()
    t.right(-90)
    t.fd(100)
    t.penup()
    if ti in [0,2,3,5,6,7,8,9]:#上
        t.pendown()
    t.right(90)
    t.fd(100)
    t.penup()
    if ti in [0,1,2,3,4,7,8,9]:#右上
        t.pendown()
    t.right(90)
    t.fd(100)
    t.penup()
    if ti in [1,3,4,5,6,7,8,9]:#右下
        t.pendown()
    t.fd(100)
    t.penup()
    if ti in [0,2,3,5,6,8,9]:#下
        t.pendown()
    t.right(90)
    t.fd(100)
    t.penup()
    if ti in [0,2,6,8]:#左下
        t.pendown()
    t.right(90)
    t.fd(100)
    t.penup()
    t.right(90)
    t.fd(300)
t.done()