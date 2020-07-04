import tkinter as tk

def rectangle(canvas,startx,starty,width,height,/,outline=None,fill=None):
    """Create a rectangle with width and height"""
    startx = abs(startx - startx % 2)
    starty = abs(starty - starty % 2)
    width  = abs(width  - width  % 2)
    height = abs(height - height % 2)
    canvas.create_rectangle(startx,starty,width,height,outline=outline,fill=fill)
    return canvas
def rectangle_wend(canvas,startx,starty,endx,endy,/,outline=None,fill=None):
    """Creates a rectangle with end x y coor"""
    width = endx - startx
    height = endy - starty
    return rectangle(canvas,startx,starty,width,height,outline=outline,fill=fill)
def poly(canvas,pt:tuple,/,outline=None,fill=None):
    """Creates a polygon"""
    canvas.create_polygon(pt,outline=outline,fill=fill)
    return canvas
class Cube:
    def __init__(self,canvas,x1,y1,x2,y2,length,**kwargs):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.length = length
        self.canvas = canvas
        self.kwargs = kwargs
    def left(self,px=1):
        self.x1 -= px*2
        self.x2 -= px
    def right(self,px=1):
        self.x1 += px*2
        self.x2 += px
    def up(self,px=1):
        self.y1 -= px*2
        self.y2 -= px
    def down(self,px=1):
        self.y1 += px*2
        self.y2 += px
    def place(self):
        x1 = self.x1
        x2 = self.x2
        y1 = self.y1
        y2 = self.y2
        length = self.length
        self.canvas.create_polygon((x1,y1,x2,y2,x2+length,y2,x2+length,y2+length,x1+length,y1+length,x1,y1+length,x1,y1,x1+length,y1,x2+length,y2,x1+length,y1,x1+length,y1+length,x1+length,y1,x1,y1),**self.kwargs)