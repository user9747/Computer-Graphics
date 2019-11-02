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
        dx = x2 - x1
        dy = y2 - y1
        yi = 1
        if dy <0:
            yi=-1
            dy=-dy
        D = 2*dy - dx
        y = y1

        for x in range(x1,x2+1):
            self.draw_dot(x,y)
            if(D>0):
                y = y+ yi
                D = D - 2*dx
            D = D + 2*dy 


l = Line("blue")
l.draw_line(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
print("Done")
time.sleep(5) 