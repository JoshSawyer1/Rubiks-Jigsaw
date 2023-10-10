#Frog Class
#Random - randomise frogs & colours
import random

class frog:

    #Class variables
    isFrog = True
    colours = ["red","orange","yellow","green","blue","white", "black"]
    
    #Initialisation function
    def __init__(self, rightArm, rightLeg, rightTorso, leftArm, leftLeg, leftTorso, head, onBoard):
        self.rightArm = rightArm
        self.rightLeg =  rightLeg
        self.rightTorso = rightTorso
        self.leftArm = leftArm
        self.leftLeg = leftLeg
        self.leftTorso = leftTorso
        self.head = head
        self.onBoard = False
        self.colourList = [rightArm, rightLeg, rightTorso, leftArm, leftLeg, leftTorso, head]
    
    # Stating frog stats through printing

    def statusColour (self):
        print("Right arm is ", self.rightArm)
        print("Right leg is ", self.rightLeg)
        print("Right torso is ", self.rightTorso)
        print("Left arm is ", self.leftArm)
        print("Left leg is ", self.leftLeg)
        print("Left torso is ", self.leftTorso)
        print("Head is ", self.head)
        print("Frog on board is", self.onBoard)
        
    #Moves colours into individual sections of frog:

    def colouring(self):
        self.rightArm = self.colourList[0]
        self.rightLeg = self.colourList[1]
        self.rightTorso = self.colourList[2]
        self.leftArm = self.colourList[3]
        self.leftLeg = self.colourList[4]
        self.leftTorso = self.colourList[5]
        self.head = self.colourList[6]

    #Ranomly colouring frogs
    def randomColouring (self):
        
