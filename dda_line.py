import turtle
import time
import math
import sys

class Line:
    def __init__(self,clr):
        turtle.setup(800, 600)
        wn = turtle.Screen()
        turtle.color(clr)
        turtle.pensize(-4)
        turtle.penup()

    def draw_dot(self,p1,p2):
        turtle.setpos(p1,p2)
        print(p1,p2)
        turtle.dot()
   

    def draw_line(self,x1,y1,x2,y2):
        x=float(x1)
        y=float(y1)
        self.draw_dot(x,y)
        dx=float(x2-x1)
        dy=float(y2-y1)
        length = int(max(abs(dx),abs(dy)))
        x_inc = dx/length
        y_inc = dy/length
        for i in range(1,length):
            x=x + x_inc
            y=y + y_inc
            self.draw_dot(math.ceil(x),math.ceil(y))


l = Line("blue")
l.draw_line(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
print("Done")
time.sleep(5) 