import tkinter as tk
import os,draw,sys,os,platform,time
from constant import *

item = {
    'cube': {
        'size': 100,
        'startx': 200,
        'starty': 0
    }
}

moves = {
    'w': False,
    's': False
}

def kp(event):
    global root,moves
    if event.keysym == "Escape":
        root.destroy()
        quit()
        return
    if event.keysym == 'w':
        moves['w'] = True
    if event.keysym == 's':
        moves['s'] = True
    if event.keysym == 'a':
        moves['a'] = True
    if event.keysym == 'd':
        moves['d'] = True
def kr(event):
    global moves
    if event.keysym == 'w':
        moves['w'] = False
    if event.keysym == 's':
        moves['s'] = False
    if event.keysym == 'a':
        moves['a'] = False
    if event.keysym == 'd':
        moves['d'] = False

def main():
    global moves,root,item
    root = tk.Tk()
    root.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
    root.title('tk3d test')
    root.update()

    root.bind_all('<KeyPress>', kp)
    root.bind_all('<KeyRelease>', kr)
    while True:
        try:
            WIDTH = root.winfo_width()
            HEIGHT= root.winfo_height()
            if moves['w']:
                item['cube']['size'] += 1.005
                # item['cube']['startx'] *= 1.01
                item['cube']['startx'] /= 1.01
                # item['cube']['starty'] *= 1.01
                item['cube']['starty'] *= 1.01
            if moves['s']:
                item['cube']['size'] -= 1.005
                # item['cube']['startx'] /= 1.01
                item['cube']['startx'] *= 1.01
                # item['cube']['starty'] /= 1.01
                item['cube']['starty'] /= 1.01

            c = tk.Canvas(root,width=WIDTH, height=HEIGHT)
            cube = draw.Cube(c,50,100,100,50,100,outline='#fff')
            cube.up(20)
            cube.place()
            c.place(x=0,y=0)


            root.update()
            time.sleep(0.005)
        except tk._tkinter.TclError:
            return 0
if __name__ == "__main__":
    main()