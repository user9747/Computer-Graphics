__author__ = "Albin Antony"
__license__ = "GPL"
__version__ = "1.0.1"


import turtle
import time
import math
import sys
import numpy as np

class Line:
    def __init__(self,clr):
        turtle.setup(1366, 768)
        wn = turtle.Screen()
#axis
        turtle.setpos(0, 0)
        turtle.color("black")
        turtle.pensize(1)
        turtle.tracer(0, 0)
        for i in range(4):
            turtle.fd(300)
            turtle.pu()
            turtle.goto(0, 0)
            turtle.pd()
            turtle.lt(90)
        turtle.ht()
#lines
        turtle.color(clr)
        turtle.pensize(-4)
        turtle.penup()
        turtle.speed(-1)
        


    def draw_dot(self,p1,p2):
        turtle.setpos(p1,p2)
        print(p1,p2)
        turtle.dot()
        turtle.update()
   

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

class Triangle(Line):
    def __init__(self,clr):
        super().__init__(clr)
    def draw_triangle(self,px,py,qx,qy,rx,ry):
        super().draw_line(px,py,qx,qy)
        super().draw_line(qx,qy,rx,ry)
        super().draw_line(rx,ry,px,py)
        turtle.hideturtle()
    def rotate(self,px,py,qx,qy,rx,ry):
        turtle.color("red")
        T = ([1,0,-px],
             [0,1,-py],
             [0,0, 1 ])
        R = ([np.cos(np.deg2rad(90)),-np.sin(np.deg2rad(90)),0],
             [np.sin(np.deg2rad(90)),np.cos(np.deg2rad(90)) ,0],
             [0         ,0          ,1])

        T_inv = ([1,0,px],
                 [0,1,py],
                 [0,0,1 ])

        res = np.dot(T_inv,np.dot(R,T))
        print(res)
        p = np.dot(res,[px,py,1])
        q = np.dot(res,[qx,qy,1])
        r = np.dot(res,[rx,ry,1])
        self.draw_triangle(p[0],p[1],q[0],q[1],r[0],r[1])
        
    def scale(self,px,py,qx,qy,rx,ry):
        turtle.color("green")
        T = ([1,0,-qx],
             [0,1,-qy],
             [0,0, 1 ])
        S = ([2, 0,1],
             [0,.5,1],
             [0, 0,1])

        T_inv = ([1,0,qx],
                 [0,1,qy],
                 [0,0,1 ])

        res = np.dot(T_inv,np.dot(S,T))
        print(res)
        p = np.dot(res,[px,py,1])
        q = np.dot(res,[qx,qy,1])
        r = np.dot(res,[rx,ry,1])
        self.draw_triangle(p[0],p[1],q[0],q[1],r[0],r[1])

    def reflect(self,px,py,qx,qy,rx,ry):
        turtle.color("blue")
        Ref = ([-1, 0,0],
               [ 0, 1,0],
               [ 0, 0,1])

        p = np.dot(Ref,[px,py,1])
        q = np.dot(Ref,[qx,qy,1])
        r = np.dot(Ref,[rx,ry,1])
        self.draw_triangle(p[0],p[1],q[0],q[1],r[0],r[1])
        
        

        
        


# l = Line("blue")
# l.draw_line(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
l = Triangle("blue")
l.draw_triangle(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]))
l.rotate(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]))
l.scale(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]))
l.reflect(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]))


print ("Done")
time.sleep(50) 