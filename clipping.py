__author__ = "Albin Antony"
__license__ = "GPL"
__version__ = "1.0.1"
#Sutherland-Hodgman Algorithm

import turtle
import time
import math
import sys

class Line:
    def __init__(self,clr):
        turtle.setup(1366, 768)
        wn = turtle.Screen()
        turtle.color(clr)
        turtle.pensize(-4)
        turtle.penup()
        turtle.speed('fastest')
        turtle.tracer(0, 0)
        

    def draw_dot(self,p1,p2):
        turtle.setpos(p1,p2)
        # print(p1,p2)
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
        

    def draw_polygon(self,list,clr):
        turtle.color(clr)
        for i in range(0,len(list),2):
            self.draw_line(list[i],list[i+1],list[(i+2)%len(list)],list[(i+3)%len(list)])

    def x_intersect(self,x1,y1,x2,y2,x3,y3,x4,y4): 
        num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4); 
        den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4); 
        return num/den; 

    def y_intersect(self,x1,y1,x2,y2,x3,y3,x4,y4): 
        num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4); 
        den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4); 
        return num/den; 
    
    def clip(self,poly_list,x1,y1,x2,y2):
        new_poly_list = []
        for i in range(0,len(poly_list),2):
            ix = poly_list[i]
            iy = poly_list[i+1]
            kx = poly_list[(i+2)%len(poly_list)]
            ky = poly_list[(i+3)%len(poly_list)]
            i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1)
            k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1)
            print(ix,iy," ",kx,ky)
            print(i_pos,k_pos)
            if (i_pos < 0  and k_pos < 0):
                new_poly_list.append(kx)
                new_poly_list.append(ky)
                
            
            elif (i_pos >= 0  and k_pos < 0):
                new_poly_list.append(self.x_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
                print("x",self.x_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
                new_poly_list.append(self.y_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
                print("y",self.y_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
                new_poly_list.append(kx)
                new_poly_list.append(ky)

            elif (i_pos < 0  and k_pos >= 0):
                new_poly_list.append(self.x_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
                new_poly_list.append(self.y_intersect(x1,y1, x2, y2, ix, iy, kx, ky))
                

            
        return new_poly_list

    def suthHodgClip(self,poly_list,clipper_list,clr):
        for i in range(0,len(clipper_list),2):
            print("h",poly_list) 
            poly_list=self.clip(poly_list,clipper_list[i],clipper_list[i+1],clipper_list[(i+2)%len(clipper_list)],clipper_list[(i+3)%len(clipper_list)])
        self.draw_polygon(poly_list,clr)
        return poly_list
        


l = Line("blue")
poly_list = []
for i in range(int(sys.argv[1])*2):
    poly_list.append(int(sys.argv[i+2]))
 
l.draw_polygon(poly_list,"blue")
# clipper_list = [150,150,150,200,200,200,200,150]
# 10,10,80,10,80,70,10,70]
clipper_list = [10,70,80,70,80,10,10,10]
l.draw_polygon(clipper_list,"red")
poly_list = l.suthHodgClip(poly_list,clipper_list,"black")
print(poly_list)
# turtle.resetscreen()
# k = Line("blue")
# k.draw_polygon(poly_list,"blue")
turtle.hideturtle()
print("Done")
time.sleep(500) 