import tkinter as tk
import math

win=tk.Tk()
h=800
w=800
d=800

def sierp(a,b,d,hlbka=6):
    if hlbka>0:
        hlbka-=1
        canvas.create_rectangle(a,b,a+d,b+d)
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1: sierp(a+i*(d//3), b+j*(d//3), d//3, hlbka)

def sierpin(x,y,a,count=0):
    if count<5:
        count+=1
        for i in range(3):
            canvas.create_rectangle((i*a)//3+x, 0+y, ((i+1)*a)//3+x, a//3+y, fill='white', outline='black')
        canvas.create_rectangle(0+x, a//3+y, a//3+x, (2*a)//3+y, fill='white', outline='black')
        canvas.create_rectangle((2*a)//3+x, a//3+y, a+x, (2*a)//3+y, fill='white', outline='black')
        for i in range(3):
            canvas.create_rectangle((i*a)//3+x, (2*a)//3+y, ((i+1)*a)//3+x, a+y, fill='white', outline='black')

        for i in range(3):
            sierpin((i*a)//3+x, 0+y, a//3, count)
        sierpin(0+x, a//3+y, a//3, count)
        sierpin((2*a)//3+x, a//3+y, a//3, count)
        for i in range(3):
            sierpin((i*a)//3+x, (2*a)//3+y, a//3, count)

canvas=tk.Canvas(win,height=h,width=w,bg="white")
canvas.pack()
sierp(10,10,d)
sierpin(10,10,d)
win.mainloop()
