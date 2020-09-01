import tkinter as tk
import math
import logging


logger = logging.Logger("draw")
class Coor2d:
    """a class that stores 2d coordinates"""

    def __init__(self, x, y, *, fov=(7, 42)):
        x = x // 4 * 4
        y = y // 4 * 4
        self.x = x
        self.y = y
        self.fov = fov
        logger.debug(f"created 2d coor ({x}, {y})")


class Coor3d:
    """a class that stores 3d coordinates"""

    def __init__(self, x, y, z, *, fov=(7, 42)):
        self.x = x
        self.y = y
        self.z = z
        self.fov = fov
        logger.debug(f"created 3d coor ({x}, {y}, {z})")

    def to_2d(self):
        return Coor2d(
            self.x * math.cos(self.fov[0]) + self.z *
            math.cos(self.fov[1]) / 2,
            self.y + self.z *
            math.sin(self.fov[1]) / 2 - self.x * math.sin(self.fov[0])
        )


def rectangle(canvas, startx, starty, width, height, /, outline=None, fill=None):
    """Create a rectangle with width and height"""
    startx = abs(startx - startx % 2)
    starty = abs(starty - starty % 2)
    width = abs(width - width % 2)
    height = abs(height - height % 2)
    canvas.create_rectangle(startx, starty, width,
                            height, outline=outline, fill=fill)
    return canvas


def rectangle_wend(canvas, startx, starty, endx, endy, /, outline=None, fill=None):
    """Creates a rectangle with end x y coor"""
    width = endx - startx
    height = endy - starty
    return rectangle(canvas, startx, starty, width, height, outline=outline, fill=fill)


def poly(canvas, pts: tuple, /, outline=None, fill=None):
    """Creates a polygon"""
    canvas.create_polygon(pts, outline=outline, fill=fill)
    return canvas


class Polygon:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.pts = list()

    def add_pt(self, coor: Coor2d):
        self.pts.append(coor)

    def place(self, **kwargs):
        return poly(self.canvas, self.pts, **kwargs)


class Polyhedra:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.pts = list()

    def add_pt(self, coor: Coor3d):
        self.pts.append(coor)

    def place(self, **kwargs):
        pts2d = list()
        for pt in self.pts:
            tmp = pt.to_2d()
            pts2d.append(tmp.x)
            pts2d.append(tmp.y)
        poly(self.canvas, pts2d, **kwargs)


class Cube(Polyhedra):
    def __init__(self, canvas: tk.Canvas, coor: Coor3d, length: int):
        self.coor = coor
        self.length = length
        super().__init__(canvas)

    def place(self, **kwargs):
        length, coor = self.length, self.coor
        # ===================# back of the cube
        b1 = b2 = b3 = coor  # b1: bottom left up
        b2.x += length      # b2: bottom right up
        b3.y += length      # b3: bottom left bottom
        b4 = b3             # b4: bottom right bottom
        b4.x += length
        # ===================# front of the cube
        f1 = coor
        f1.z += length      # b1: bottom left up
        f2 = f3 = f1        # b2: bottom right up
        f2.x += length      # b3: bottom left bottom
        f3.y += length      # b4: bottom right bottom
        f4 = f3
        f4.x += length
        self.pts = [f1, f3, f4, f2, f1, b1, b2, f2, f4, b4, b2]
        return super().place(**kwargs)


if __name__ == "__main__":
    coor2d = Coor3d(1, 1, 1).to_2d()
    print(coor2d.x)
    print(coor2d.y)
