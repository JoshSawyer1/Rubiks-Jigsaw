# Board
import tkinter
import math as maths
import random
from frogclass import frog
import pickle

# Create a Tkinter window
window = tkinter.Tk()

# Create a canvas widget with a white background and specified dimensions
canvas = tkinter.Canvas(window, bg="black", height=1200, width=1500)

scale = 0.6
# Initialize a counter variable
counter = 0
colours = ["sky blue","red","green","orange","white","yellow"]

# Loop to draw a pattern of diagonal lines
for i in range(100):
    x1 = 0
    if counter % 2 == 0:
        # Calculate the starting y-coordinate for even rows
        y1 = (i * ((27 * maths.sqrt(3)) / 3))*scale
        inc = ((27 * maths.sqrt(3)) / 3)*scale
    else:
        # Calculate the starting y-coordinate for odd rows
        inc = -((27 * maths.sqrt(3)) / 3)*scale

    # Loop to draw diagonal lines in a row
    for z in range(64):
        x2 = x1 + (27*scale)
        y2 = y1 + inc
        colour = random.choice(colours)
       
        # Create a line on the canvas from (x1, y1) to (x2, y2)
        line = canvas.create_line(x1, y1, x2, y2, fill='white')

        x1 = x2
        y1 = y2

        # Toggle the inclination for the next line
        if inc == ((27 * maths.sqrt(3)) / 3)*scale:
            inc = -((27 * maths.sqrt(3)) / 3)*scale
        else:
            inc = ((27 * maths.sqrt(3)) / 3)*scale

    counter += 1

# Initialize coodinates for drawing vertical lines
x1 = 0
y1 = 0
y2 = 0

# Loop to draw vertical lines
for p in range(100):
    # Calculate the coordinates of the top and bottom vertices
    x2 = x1 
    y2 = y1 + (2700*scale)

    # Create a vertical line on the canvas from (x1, y1) to (x2, y2)
    line = canvas.create_line(x1, y1, x2, y2, fill="white")

    x1 += 27*scale

# Unpickle grid
f = open("frogspaghetti.txt", "rb")
grid = pickle.load(f)
print(grid)
f.close()

# Place frogs
counter = 1
grid_x = 0
grid_y = 0
x_start = 27*scale
x = x_start 
y = (54*maths.sqrt(3))*scale
y_start = (54*maths.sqrt(3))*scale
for i in range(9):
    if counter%2 == 0:
        x = x_start +(162*scale)
    else:
        x = x_start+(81*scale)
    for z in range(9):
        current = grid[grid_x][grid_y]
        Head_polygon = canvas.create_polygon(x+(81*scale),y+(45*maths.sqrt(3)*scale),x+(162*scale),y+(18*maths.sqrt(3)*scale),x+(243*scale),y+(45*maths.sqrt(3)*scale),x+(162*scale),y+(72*maths.sqrt(3)*scale),x+(81*scale),y+(45*maths.sqrt(3)*scale),fill=current.Head)
        LArm_polygon = canvas.create_polygon(x+(162*scale),y-((18*maths.sqrt(3))*scale),x+(216*scale),y,x+(216*scale),y+((18*maths.sqrt(3))*scale),x+(162*scale),y,fill=current.LArm)
        RArm_polyon = canvas.create_polygon(x+(162*scale),y+(108*maths.sqrt(3)*scale),x+(216*scale), y+(90*maths.sqrt(3)*scale),x+(216*scale),y+(72*maths.sqrt(3)*scale),x+(162*scale), y+(90*maths.sqrt(3)*scale),fill=current.RArm)
        LTorso_polygon = canvas.create_polygon(x+(81*scale),y+(27*maths.sqrt(3)*scale),x+(135*scale),y+(9*maths.sqrt(3)*scale),x+(135*scale),y-(9*maths.sqrt(3)*scale),x+(162*scale),y-(18*maths.sqrt(3)*scale),x+(162*scale),y,x+(162*scale),y+(18*maths.sqrt(3)*scale),x+(81*scale),y+(45*maths.sqrt(3)*scale),x+(81*scale),y+(27*maths.sqrt(3)*scale), fill=current.LTorso)
        RTorso_polygon = canvas.create_polygon(x+(81*scale),y+(45*maths.sqrt(3)*scale),x+(81*scale),y+(63*maths.sqrt(3)*scale),x+(135*scale),y+(81*maths.sqrt(3)*scale),x+(135*scale),y+(99*maths.sqrt(3)*scale),x+(162*scale),y+(108*maths.sqrt(3)*scale),x+(162*scale),y+(72*maths.sqrt(3)*scale),x+(81*scale),y+(35*maths.sqrt(3*scale)), fill=current.RTorso)
        LLeg_polygon = canvas.create_polygon(x,y,x+(81*scale),y+(27*maths.sqrt(3)*scale),x+(81*scale),y+(45*maths.sqrt(3)*scale),x,y+(18*maths.sqrt(3)*scale),x,y, fill=current.LLeg)
        RLeg_polygon = canvas.create_polygon(x+(81*scale),y+(45*maths.sqrt(3)*scale),x+(81*scale),y+(63*maths.sqrt(3)*scale),x,y+(90*maths.sqrt(3)*scale),x,y+(72*maths.sqrt(3)*scale),x+(81*scale),y+(45*maths.sqrt(3)*scale), fill=current.RLeg)
        x = x + (162*scale)
        if grid_x == 8:
            grid_x = 0
            grid_y += 1
        else:
            grid_x += 1
    y = y_start+(((i+1)*81*maths.sqrt(3))*scale)
    counter += 1

#Border frog placing
counter = 1
grid_x = 0
grid_y = 0
x_start = 27*scale
x = x_start 
y = (54*maths.sqrt(3))*scale
y_start = (54*maths.sqrt(3))*scale
#Left side
for i in range(1):
    y = y_start
    for z in range(5): #Non-irregular frog formation
        Triangle_Border1 = canvas.create_polygon(x,y-(9*maths.sqrt(3)*scale),x+(81*scale),y-(36*maths.sqrt(3)*scale),x,y-(63*maths.sqrt(3)*scale),fill = 'white')
        Square_Border1 = canvas.create_polygon(x,y+(45*maths.sqrt(3)*scale),x+(81*scale),y+(18*maths.sqrt(3)*scale),x+(81*scale),y-(36*maths.sqrt(3)*scale),x,y-(9*maths.sqrt(3)*scale),fill='sky blue')
        Head_Border1 = canvas.create_polygon(x,y+(45*maths.sqrt(3)*scale),x+(81*scale),y+(18*maths.sqrt(3)*scale),x+(162*scale),y+(45*maths.sqrt(3)*scale),x+(81*scale),y+(72*maths.sqrt(3)*scale),x,y+(45*maths.sqrt(3)*scale),fill='magenta')
        Square_Border2 = canvas.create_polygon(x,y+(45*maths.sqrt(3)*scale),x+(81*scale),y+(72*maths.sqrt(3)*scale),x+(81*scale),y+(126*maths.sqrt(3)*scale),x,y+(99*maths.sqrt(3)*scale), fill='cyan')
        y = y + (280*scale)
        for a in range (6): #Creates the bottom triangle
            Triangle_Border1 = canvas.create_polygon(x,y-(9*maths.sqrt(3)*scale),x+(81*scale),y-(36*maths.sqrt(3)*scale),x,y-(63*maths.sqrt(3)*scale),fill = 'white')
#Irregular frog placement
y = y_start
for s in range (4):
    Deformed_LTorso = canvas.create_polygon(x+(81*scale),y+(90*maths.sqrt(3)*scale),x+(162*scale),y+(63*maths.sqrt(3)*scale),x+(162*scale),y+(99*maths.sqrt(3)*scale),x+(81*scale),y+(126*maths.sqrt(3)*scale), fill = 'sky blue')
    Deformed_LArm = canvas.create_polygon(x+(162*scale),y+(63*maths.sqrt(3)*scale),x+(216*scale),y+(81*maths.sqrt(3)*scale),x+(216*scale),y+(99*maths.sqrt(3)*scale),x+(162*scale),y+(81*maths.sqrt(3)*scale), fill = 'cyan')
    Deformed_Head = canvas.create_polygon(x+(81*scale),y+(126*maths.sqrt(3)*scale),x+(162*scale),y+(99*maths.sqrt(3)*scale),x+(243*scale),y+(126*maths.sqrt(3)*scale),x+(162*scale),y+(153*maths.sqrt(3)*scale), fill = 'magenta')
    Deformed_RTorso = canvas.create_polygon(x+(81*scale),y+(126*maths.sqrt(3)*scale),x+(162*scale),y+(153*maths.sqrt(3)*scale),x+(162*scale),y+(189*maths.sqrt(3)*scale),x+(81*scale),y+(162*maths.sqrt(3)*scale), fill ='green')
    Deformed_RArm = canvas.create_polygon(x+(162*scale),y+(171*maths.sqrt(3)*scale),x+(216*scale),y+(153*maths.sqrt(3)*scale),x+(216*scale),y+(171*maths.sqrt(3)*scale),x+(162*scale),y+(189*maths.sqrt(3)*scale), fill = 'brown')
    y = y + (280*scale)











    
# Pack the canvas widget into the window
canvas.pack()

# Start the Tkinter main loop
window.mainloop()


# End lol
