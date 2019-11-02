import turtle
import time
import math
import sys

class Circle:
    def __init__(self,clr,x,y):
        self.cen_x = x
        self.cen_y = y
        turtle.setup(800, 600)
        wn = turtle.Screen()
        turtle.pensize(-4)
        turtle.color(clr)
        turtle.penup()
        turtle.speed(-1)

    def draw_dot(self,p1,p2):
        turtle.setpos(p1+self.cen_x,p2+self.cen_y)
        print(p1,p2)
        turtle.dot()

        turtle.setpos(p2+self.cen_x,p1+self.cen_y)
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p2+self.cen_x,p1+self.cen_y)
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p1+self.cen_x,p2+self.cen_y)
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p1+self.cen_x,-p2+self.cen_y)
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p2+self.cen_x,-p1+self.cen_y)
        print(p1,p2)
        turtle.dot()
        
        turtle.setpos(p2+self.cen_x,-p1+self.cen_y)
        print(p1,p2)
        turtle.dot()

        turtle.setpos(p1+self.cen_x,-p2+self.cen_y)
        print(p1,p2)
        turtle.dot()

    def draw_circle(self,r):
        p= 1-r
        x=r
        y=0
        while(y<=x):
            self.draw_dot(x,y)
            if(p<=0):
                p=p+2*y+3
                y=y+1
            else:
                p=p+2*y-2*x+5
                y=y+1
                x=x-1

c = Circle("blue",int(sys.argv[1]),int(sys.argv[2]))
c.draw_circle(int(sys.argv[3]))
print("Done")
time.sleep(5) 