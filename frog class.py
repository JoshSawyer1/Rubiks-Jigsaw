# Frog class
# Randomise frogs + colours
import random

class frog:
    # Class variables
    isFrog = True
    colours = ("white", "yellow", "red", "green", "blue", "orange")

    # Def function for frogs, not same frog. sets 'self' for frogs.
    def __init__(self, RArm, LArm, RTorso, LTorso, RLeg, LLeg, Head):
        self.RArm = right_arm
        self.LArm = left_arm
        self.RTorso = right_torso
        self.LTorso = left_torso
        self.RLeg = right_leg
        self.LLeg = left_leg
        self.Head = head
        self.colourList = (right_arm, left_arm, right_torso, left_torso, right_leg, left_leg, head)

    # Moves colours into sections of frog
    def colourFrog(self):
        self.RArm = self.colourList[0]
        self.LArm = self.colourList[1]
        self.RTorso = self.colourList[2]
        self.LTorso = self.colourList[3]
        self.RLeg = self.colourList[4]
        self.LLeg = self.colourList[5]
        self.Head = self.colourList[6]

    # Random colours
    def randomColourFrog(self):
        
