# ked prd nefunguje tak sa na to nevyprdni a dorob to tak aby prd prdel - pato, 15.9.23

import tkinter as tk
import math

win=tk.Tk()
canvas=tk.Canvas(win, height=800, width=800, bg="white")
canvas.pack()

def sierpinski_shape(x,y,a,depth,angles):
    if depth==0:
        return
    step=a/3
    coords=[]
    for angle in angles:
        dx=step*math.cos(angle)
        dy=step*math.sin(angle)
        coords.append((x+dx,y+dy))
    for i in range(len(coords)):
        x0,y0=coords[i]
        x1,y1=coords[(i+1)%len(coords)]
        canvas.create_line(x0,y0,x1,y1,fill='black')
        sierpinski_shape(x0,y0,a/3,depth-1,angles)

def sierpinski_carpet(x,y,a,depth=4):
    if depth==0:
        return
    angles=[0, math.pi/3, 2*math.pi/3, math.pi, 4*math.pi/3, 5*math.pi/3]
    for i in range(6):
        sierpinski_shape(x,y,a,depth,angles)
        x+=a/2*math.cos(angles[i])
        y+=a/2* math.sin(angles[i])

sierpinski_carpet(10,10,800)
win.mainloop()
