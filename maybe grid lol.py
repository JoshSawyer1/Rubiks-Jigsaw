import tkinter
import math as maths

window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg="white", height=1000, width=1000)

counter = 0
for i in range(200):
    x1 = 10
    if counter%2 == 0:
        y1 = (i*((10*maths.sqrt(3))/3))
        inc = ((10*maths.sqrt(3))/3)
    else:
        inc = -((10*maths.sqrt(3))/3)
    for z in range(100):
        x2 = x1 + 10
        y2 = y1 + inc
        line = canvas.create_line(x1, y1, x2, y2)
        x1 = x2
        y1 = y2
        if inc == ((10*maths.sqrt(3))/3):
            inc = -((10*maths.sqrt(3))/3)
        else:
            inc = ((10*maths.sqrt(3))/3)
    counter += 1

x1 = 10
y1 = 0
y2 = 1000
for p in range(100):
    line = canvas.create_line(x1,y1,x1,y2)
    x1 += 10
canvas.pack()
