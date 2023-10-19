# Input screen
# Import libraries
import tkinter
import math as maths
from frog import frog
import pickle

# Set window and canvas geometry
window = tkinter.Tk()
window.geometry("500x350")
window.title("Input screen")
canvas = tkinter.Canvas(window, bg="black", height=250, width=270)

# Set counters and colours
colours = ["white","yellow","green","blue","red","orange"]
Head_counter = 1
LArm_counter = 1
RArm_counter = 1
LTorso_counter = 1
RTorso_counter = 1
LLeg_counter = 1
RLeg_counter = 1

# Create empty board to name frogs
grid_x = 0
grid_y = 0
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
grid = [a,b,c,d,e,f,g,h,i]

# Open file for handling
f = open("froglist.txt","wb")

# Define the setting functions that toggle each colour
def set_LArm():
    global LArm_counter
    LArm_polygon = canvas.create_polygon(x+162,y-(18*maths.sqrt(3)),x+216,y,x+216,y+(18*maths.sqrt(3)),x+162,y,fill=colours[LArm_counter])
    if LArm_counter == 5:
        LArm_counter = 0
    else:
        LArm_counter += 1

def set_RArm():
    global RArm_counter
    RArm_polygon = canvas.create_polygon(x+162,y+(108*maths.sqrt(3)),x+216, y+(90*maths.sqrt(3)),x+216, y+(72*maths.sqrt(3)),x+162, y+(90*maths.sqrt(3)),fill=colours[RArm_counter])
    if RArm_counter == 5:
        RArm_counter = 0
    else:
        RArm_counter += 1

def set_LTorso():
    global LTorso_counter
    LTorso_polygon = canvas.create_polygon(x+81,y+(27*maths.sqrt(3)),x+135,y+(9*maths.sqrt(3)),x+135,y-(9*maths.sqrt(3)),x+162,y-(18*maths.sqrt(3)),x+162,y,x+162,y+(18*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x+81,y+(27*maths.sqrt(3)), fill=colours[LTorso_counter])
    if LTorso_counter == 5:
        LTorso_counter = 0
    else:
        LTorso_counter += 1

def set_RTorso():
    global RTorso_counter
    RTorso_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x+135,y+(81*maths.sqrt(3)),x+135,y+(99*maths.sqrt(3)),x+162,y+(108*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill=colours[RTorso_counter])
    if RTorso_counter == 5:
        RTorso_counter = 0
    else:
        RTorso_counter += 1

def set_LLeg():
    global LLeg_counter
    LLeg_polygon = canvas.create_polygon(x,y,x+81,y+(27*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x,y+(18*maths.sqrt(3)),x,y, fill=colours[LLeg_counter])
    if LLeg_counter == 5:
        LLeg_counter = 0
    else:
        LLeg_counter += 1

def set_RLeg():
    global RLeg_counter
    RLeg_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x,y+(90*maths.sqrt(3)),x,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill=colours[RLeg_counter])
    if RLeg_counter == 5:
        RLeg_counter = 0
    else:
        RLeg_counter += 1

def set_Head():
    global Head_counter
    Head_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+162,y+(18*maths.sqrt(3)),x+243,y+(45*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),fill=colours[Head_counter])
    if Head_counter == 5:
        Head_counter = 0
    else:
        Head_counter += 1

# Create function to append frogs to grid
def submit_frog():
    global grid_x
    global grid_y
    grid[grid_x].append(frog(colours[RArm_counter],colours[LArm_counter],colours[RTorso_counter],colours[LTorso_counter],colours[RLeg_counter],colours[LLeg_counter],colours[Head_counter]))
    if grid_x == 8:
        grid_x = 0
        grid_y += 1
    else:
        grid_x += 1

# Create function to store grid
def submit_grid():
    global grid
    pickle.dump(grid, f)

# Close file
def close_file():
    f.close()

# Placement of buttons
LArm_button = tkinter.Button(window, command=set_LArm, text="Left arm").place(x=10,y=40)
RArm_button = tkinter.Button(window, command=set_RArm, text="Right arm").place(x=10,y=70)
LTorso_button = tkinter.Button(window, command=set_LTorso, text="Left torso").place(x=10,y=100)
RTorso_button = tkinter.Button(window, command=set_RTorso, text="Right torso").place(x=10,y=130)
LLeg_button = tkinter.Button(window, command=set_LLeg, text="Left leg").place(x=10,y=160)
RLeg_button = tkinter.Button(window, command=set_RLeg, text="Right leg").place(x=10,y=190)
Head_button = tkinter.Button(window, command=set_Head, text="Head").place(x=10,y=10)

submit_frog_button = tkinter.Button(window, command=lambda: submit_frog(), text="Submit frog").place(x=10, y=250)
submit_grid_button = tkinter.Button(window, command=lambda: submit_grid(), text="Submit grid").place(x=10, y=280)
close_file_button = tkinter.Button(window, command=lambda: close_file(), text="Close file").place(x=10, y=310)

# Creating initial polygon
x = 20
y = 50

LArm_polygon = canvas.create_polygon(x+162,y-(18*maths.sqrt(3)),x+216,y,x+216,y+(18*maths.sqrt(3)),x+162,y,fill="white")
LTorso_polygon = canvas.create_polygon(x+81,y+(27*maths.sqrt(3)),x+135,y+(9*maths.sqrt(3)),x+135,y-(9*maths.sqrt(3)),x+162,y-(18*maths.sqrt(3)),x+162,y,x+162,y+(18*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x+81,y+(27*maths.sqrt(3)), fill="white")
RArm_polygon = canvas.create_polygon(x+162,y+(108*maths.sqrt(3)),x+216, y+(90*maths.sqrt(3)),x+216, y+(72*maths.sqrt(3)),x+162, y+(90*maths.sqrt(3)),fill="white")
RTorso_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x+135,y+(81*maths.sqrt(3)),x+135,y+(99*maths.sqrt(3)),x+162,y+(108*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill="white")
LLeg_polygon = canvas.create_polygon(x,y,x+81,y+(27*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x,y+(18*maths.sqrt(3)),x,y, fill="white")
RLeg_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x,y+(90*maths.sqrt(3)),x,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill="white")
Head_polygon = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+162,y+(18*maths.sqrt(3)),x+243,y+(45*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),fill="white")

# Packing and ending main loop
canvas.pack(padx=10,pady=20)
window.mainloop()

# End lol
