import tkinter
import math as maths
from frog import frog

window = tkinter.Tk()
window.geometry("500x300")
window.title("Input screen")

canvas = tkinter.Canvas(window, bg="black", height=250, width=270)

def set_left_leg():
    
    left_leg = canvas.create_polygon(x,y,x+81,y+(27*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x,y+(18*maths.sqrt(3)),x,y, fill="white")

head_button = tkinter.Button(window, text="Head").place(x=10,y=10)
LA_button = tkinter.Button(window, text="Left arm").place(x=10,y=40)
RA_button = tkinter.Button(window, text="Right arm").place(x=10,y=70)
LT_button = tkinter.Button(window, text="Left torso").place(x=10,y=100)
RT_button = tkinter.Button(window, text="Right torso").place(x=10,y=130)
LL_button = tkinter.Button(window, text="Left leg").place(x=10,y=160)
RL_button = tkinter.Button(window, text="Right leg").place(x=10,y=190)

x = 20
y = 50

left_leg = canvas.create_polygon(x,y,x+81,y+(27*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x,y+(18*maths.sqrt(3)),x,y, fill="white")
right_leg = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x,y+(90*maths.sqrt(3)),x,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill="red")
right_torso = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+81,y+(63*maths.sqrt(3)),x+135,y+(81*maths.sqrt(3)),x+135,y+(99*maths.sqrt(3)),x+162,y+(108*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)), fill="orange")
left_torso = canvas.create_polygon(x+81,y+(27*maths.sqrt(3)),x+135,y+(9*maths.sqrt(3)),x+135,y-(9*maths.sqrt(3)),x+162,y-(18*maths.sqrt(3)),x+162,y,x+162,y+(18*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),x+81,y+(27*maths.sqrt(3)), fill="green")
head = canvas.create_polygon(x+81,y+(45*maths.sqrt(3)),x+162,y+(18*maths.sqrt(3)),x+243,y+(45*maths.sqrt(3)),x+162,y+(72*maths.sqrt(3)),x+81,y+(45*maths.sqrt(3)),fill="blue")
left_arm = canvas.create_polygon(x+162,y-(18*maths.sqrt(3)),x+216,y,x+216,y+(18*maths.sqrt(3)),x+162,y,fill="yellow")
right_arm = canvas.create_polygon(x+162,y+(108*maths.sqrt(3)),x+216, y+(90*maths.sqrt(3)),x+216, y+(72*maths.sqrt(3)),x+162, y+(90*maths.sqrt(3)),fill="white")

canvas.pack(padx=10,pady=20)
window.mainloop()
