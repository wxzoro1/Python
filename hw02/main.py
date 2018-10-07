import turtle as t
import math
t.speed(10) 
t.ht()
#构造国旗矩形函数 (3：2)
def draw_rect(a,b):
    t.fillcolor('#DD2910')  #中国红  #DD2910  #五星黄  #FEDF00 
    t.pencolor('#DD2910')
    t.begin_fill()
    t.goto(-a/2,b/2)
    for x in range(2):
        t.fd(a)
        t.rt(90)
        t.fd(b)
        t.rt(90)
    t.end_fill()
#画五角星函数 需要条件:（圆心坐标（中心为原点），外接圆半径，圆心到某顶点与水平夹角） 
def draw_fpstar( Ccenter = (0,0), radius = 3 , angle = math.pi):
    t.fillcolor('#FEDF00')
    t.pencolor('#FEDF00')
    t.penup()
    t.seth(0)
    t.setpos(Ccenter)
    t.pendown()
    t.begin_fill()
    t.left(angle)
    t.fd(radius)
    t.right(162)
    for x in range(5):
        d = 2*radius*math.cos(math.pi/10)
        t.fd(d)
        t.rt(144)
    t.end_fill()
#主函数
a = t.numinput("(3:2)(建议600，400)","请输入国旗长度")
b = t.numinput("(3:2)(建议600，400)","请输入国旗宽度")
draw_rect(a,b)
draw_fpstar((-a/3,b/4),3*b/20,90)
draw_fpstar((-a/6,b*2/5),b/20,180+math.degrees(math.atan(0.6)))
draw_fpstar((-a/10,b*3/10),b/20,180+math.degrees(math.atan(1/7)))
draw_fpstar((-a/10,b*3/20),b/20,180-math.degrees(math.atan(2/7)))
draw_fpstar((-a/6,b/20),b/20,180-math.degrees(math.atan(0.8)))
t.done()