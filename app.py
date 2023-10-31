# Board
import tkinter
import math as maths
import random
from frogclass import frog
import pickle

# Create a Tkinter window
window = tkinter.Tk()

# Create a canvas widget with a white background and specified dimensions
canvas = tkinter.Canvas(window, bg="black", height=10000, width=15000)

# Initialize a counter variable
counter = 0
colours = ["sky blue","red","green","orange","white","yellow"]

# Loop to draw a pattern of diagonal lines
for i in range(100):
    x1 = 0
    if counter % 2 == 0:
        # Calculate the starting y-coordinate for even rows
        y1 = (i * ((27 * maths.sqrt(3)) / 3))
        inc = ((27 * maths.sqrt(3)) / 3)
    else:
        # Calculate the starting y-coordinate for odd rows
        inc = -((27 * maths.sqrt(3)) / 3)

    # Loop to draw diagonal lines in a row
    for z in range(100):
        x2 = x1 + 27
        y2 = y1 + inc
        colour = random.choice(colours)
       
        # Create a line on the canvas from (x1, y1) to (x2, y2)
        line = canvas.create_line(x1, y1, x2, y2, fill=colour)

        x1 = x2
        y1 = y2

        # Toggle the inclination for the next line
        if inc == ((27 * maths.sqrt(3)) / 3):
            inc = -((27 * maths.sqrt(3)) / 3)
        else:
            inc = ((27 * maths.sqrt(3)) / 3)

    counter += 1

# Initialize coodinates for drawing vertical lines
x1 = 0
y1 = 0
y2 = 0

# Loop to draw vertical lines
for p in range(100):
    # Calculate the coordinates of the top and bottom vertices
    x2 = x1
    y2 = y1 + 2700

    # Create a vertical line on the canvas from (x1, y1) to (x2, y2)
    line = canvas.create_line(x1, y1, x2, y2, fill="white")

    x1 += 27

# Unpickle grid
#f = open("frogspaghetti.txt", "rb")
#grid = pickle.load(f)
#print(grid)
#f.close()

# Place frogs
counter = 1
grid_x = 0
grid_y = 0
x_start = 27
x = x_start
y = 18*maths.sqrt(3)
y_start = 18*maths.sqrt(3)
for i in range(9):
    if counter%2 == 0:
        x = x_start
    else:
        x = x_start+81
    for z in range(9):
        #current = grid[grid_x][grid_y]
        Head_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+162,y+(18*maths.sqrt(3)),x+243,y+(45*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),fill='blue')
        LArm_polygon = canvas.create_polygon(x+162,y-(18*maths.sqrt(3)),x+216,y,x+216,y+(18*maths.sqrt(3)),x+162,y,fill='blue')
        RArm_polyon = canvas.create_polygon(x+162,y+(108*maths.sqrt(3)),x+216, y+(90*maths.sqrt(3)),x+216, y+(72*maths.sqrt(3)),x+162, y+(90*maths.sqrt(3)),fill='blue')
        LTorso_polygon = canvas.create_polygon(x+81,y+(27*maths.sqrt(3)),x+135,y+(9*maths.sqrt(3)),x+135,y-(9*maths.sqrt(3)),x+162,y-(18*maths.sqrt(3)),x+162,y,x+162,y+(18*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x+81,y+(27*maths.sqrt(3)), fill='blue')
        RTorso_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x+135,y+(81*maths.sqrt(3)),x+135,y+(99*maths.sqrt(3)),x+162,y+(108*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill='blue')
        LLeg_polygon = canvas.create_polygon(x,y,x+81,y+(27*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x,y+(18*maths.sqrt(3)),x,y, fill='blue')
        RLeg_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x,y+(90*maths.sqrt(3)),x,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill='blue')
        
        x = x + 162
        if grid_x == 8:
            grid_x = 0
            grid_y += 1
        else:
            grid_x += 1
    y = y_start+((i+1)*81*maths.sqrt(3))
    counter += 1

#Border frog placing
counter = 1
grid_x = 0
grid_y = 0
x_start = 27
x = x_start
y = 18*maths.sqrt(3)
y_start = 18*maths.sqrt(3)

for i in range(7):
    if counter%2 == 0:
        x = x_start
    else:
        x = x_start+81
    for z in range(1):
        Head_border = canvas.create_polygon(x-81,y+(45*maths.sqrt(3)),x,y+(18*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x,y+(72*maths.sqrt(3)),x-81,y+(45*maths.sqrt(3)),fill='green')
        LArm_border = canvas.create_polygon(x,y-(18*maths.sqrt(3)),x+54,y,x+54,y+(18*maths.sqrt(3)),x,y,fill='white')
        RArm_border = canvas.create_polygon(x,y+(108*maths.sqrt(3)),x+54, y+(90*maths.sqrt(3)),x+54, y+(72*maths.sqrt(3)),x, y+(90*maths.sqrt(3)),fill='white')
        LTorso_border = canvas.create_polygon(x-81,y+(27*maths.sqrt(3)),x-27,y+(9*maths.sqrt(3)),x-27,y-(9*maths.sqrt(3)),x,y-(18*maths.sqrt(3)),x,y,x,y+(18*maths.sqrt(3)),x-81,y+(45*maths.sqrt(3)),x-81,y+(27*maths.sqrt(3)), fill='sky blue')
        RTorso_border = canvas.create_polygon(x-81,y+(45*maths.sqrt(3)),x-81,y+(63*maths.sqrt(3)),x-27,y+(81*maths.sqrt(3)),x-27,y+(99*maths.sqrt(3)),x,y+(108*maths.sqrt(3)),x,y+(72*maths.sqrt(3)),x-81,y+(45*maths.sqrt(3)), fill='red')
        LLeg_border = canvas.create_polygon(x-162,y,x-81,y+(27*maths.sqrt(3)),x-81,y+(45*maths.sqrt(3)),x-162,y+(18*maths.sqrt(3)),x-162,y, fill='yellow')
        RLeg_border = canvas.create_polygon(x-81,y+(45*maths.sqrt(3)),x-81,y+(63*maths.sqrt(3)),x-162,y+(90*maths.sqrt(3)),x-162,y+(72*maths.sqrt(3)),x-81,y+(45*maths.sqrt(3)), fill='orange')
        
        x = x + 162
        if grid_x == 8:
            grid_x = 0
            grid_y += 1
        else:
            grid_x += 1
    y = y_start+((i+1)*81*maths.sqrt(3))
    counter += 1


    
# Pack the canvas widget into the window
canvas.pack()

# Start the Tkinter main loop
window.mainloop()


# End lol
