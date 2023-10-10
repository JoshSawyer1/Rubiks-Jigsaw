# Board
import tkinter
import math as maths
import random

# Create a Tkinter window
window = tkinter.Tk()

# Create a canvas widget with a white background and specified dimensions
canvas = tkinter.Canvas(window, bg="black", height=1000, width=1500)

# Initialize a counter variable
counter = 0
colours = ["sky blue","red","green","orange","white","yellow"]

# Create an empty list to store the coordinates of each vertex
vertex_coordinates = []

# Loop to draw a pattern of diagonal lines
for i in range(66):
    x1 = 0
    if counter % 2 == 0:
        # Calculate the starting y-coordinate for even rows
        y1 = (i * ((27 * maths.sqrt(3)) / 3))
        inc = ((27 * maths.sqrt(3)) / 3)
    else:
        # Calculate the starting y-coordinate for odd rows
        inc = -((27 * maths.sqrt(3)) / 3)

    # Loop to draw diagonal lines in a row
    for z in range(58):
        x2 = x1 + 27
        y2 = y1 + inc
        colour = random.choice(colours)
        
        # Create a line on the canvas from (x1, y1) to (x2, y2)
        line = canvas.create_line(x1, y1, x2, y2, fill=colour)

        # Store the coordinates of the current vertex (x2, y2)
        vertex_coordinates.append((x2, y2, colour))

        x1 = x2
        y1 = y2

        # Toggle the inclination for the next line
        if inc == ((27 * maths.sqrt(3)) / 3):
            inc = -((27 * maths.sqrt(3)) / 3)
        else:
            inc = ((27 * maths.sqrt(3)) / 3)

    counter += 1
    vertex_coordinates.append("end line")

# Initialize coodinates for drawing vertical lines
x1 = 0
y1 = 0
y2 = 0

# Loop to draw vertical lines
for p in range(56):
    # Calculate the coordinates of the top and bottom vertices
    x2 = x1
    y2 = y1 + 2700

    # Create a vertical line on the canvas from (x1, y1) to (x2, y2)
    line = canvas.create_line(x1, y1, x2, y2, fill="white")

    x1 += 27

x = 27
y = 27*maths.sqrt(3)
left_leg = canvas.create_polygon(x,y,x+81,y+(27*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x,y+(18*maths.sqrt(3)),x,y, fill="white")


# Pack the canvas widget into the window
canvas.pack()

print(vertex_coordinates)
print(len(vertex_coordinates))

# Start the Tkinter main loop
window.mainloop()


#
