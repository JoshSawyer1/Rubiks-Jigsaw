import tkinter
import math as maths

# Create a Tkinter window
window = tkinter.Tk()

# Create a canvas widget with a white background and specified dimensions
canvas = tkinter.Canvas(window, bg="white", height=1000, width=1500)

# Initialize a counter variable
counter = 0

# Loop to draw a pattern of diagonal lines
for i in range(500):
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
        
        # Create a line on the canvas from (x1, y1) to (x2, y2)
        line = canvas.create_line(x1, y1, x2, y2)
        
        x1 = x2
        y1 = y2
        
        # Toggle the inclination for the next line
        if inc == ((27 * maths.sqrt(3)) / 3):
            inc = -((27 * maths.sqrt(3)) / 3)
        else:
            inc = ((27 * maths.sqrt(3)) / 3)
    
    counter += 1

# Initialize coordinates for drawing vertical lines
x1 = 27
y1 = 0
y2 = 2700

# Loop to draw vertical lines
for p in range(300):
    # Create a vertical line on the canvas from (x1, y1) to (x1, y2)
    line = canvas.create_line(x1, y1, x1, y2)
    x1 += 27

# Pack the canvas widget into the window
canvas.pack()

# Start the Tkinter main loop
window.mainloop()
