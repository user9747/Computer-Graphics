import turtle
import time
import math
import sys

class Circle:
    def __init__(self,clr,x,y):
        self.cen_x = x
        self.cen_y = y
        turtle.setup(1388,768 )
        wn = turtle.Screen()
        turtle.color(clr)
        turtle.pensize(-4)
        turtle.penup()
        turtle.speed(-1)

    def draw_dot(self,p1,p2):
        turtle.setpos(p1+self.cen_x,p2+self.cen_y)
        turtle.color("blue")
        print(p1,p2)
        turtle.dot()

        turtle.setpos(p2+self.cen_x,p1+self.cen_y)
        turtle.color("red")
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p2+self.cen_x,p1+self.cen_y)
        turtle.color("yellow")
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p1+self.cen_x,p2+self.cen_y)
        turtle.color("green")
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p1+self.cen_x,-p2+self.cen_y)
        turtle.color("blue")
        print(p1,p2)
        turtle.dot()

        turtle.setpos(-p2+self.cen_x,-p1+self.cen_y)
        turtle.color("black")
        print(p1,p2)
        turtle.dot()
        
        turtle.setpos(p2+self.cen_x,-p1+self.cen_y)
        turtle.color("brown")
        print(p1,p2)
        turtle.dot()

        turtle.setpos(p1+self.cen_x,-p2+self.cen_y)
        turtle.color("black")
        print(p1,p2)
        turtle.dot()

    def draw_circle(self,r):
        p= 3-2*r
        x=0
        y=r
        while(x<=y):
            self.draw_dot(x,y)
            if(p<=0):
                p=p+4*x+6
                x=x+1
            else:
                p=p+4*x-4*y+10
                y=y-1
                x=x+1

c = Circle("blue",int(sys.argv[1]),int(sys.argv[2]))
c.draw_circle(int(sys.argv[3]))
print("Done")
time.sleep(5) 