import math
import random
import turtle

class Wheel:

    def __init__(self, t,size):
        self.t = t
        self.size = size
        self.RAD = 90*self.size/math.pi


    def makeCircle(self):
        self.t.penup()
        self.t.goto(0,self.RAD)
        self.t.pendown()
        for i in range(180):
           self.t.forward(self.size)
           self.t.right(2)

    def makeSectors(self,s):
        for i in range(s):
            self.t.penup()
            self.t.goto(0,0)
            self.t.pendown()
            self.t.right(360/s)
            self.t.forward(self.RAD)
        self.t.goto(0,0)

    def pickSector(self):
        self.t.setheading(0)
        r = random.randrange(75,150)
        for i in range(r):
            self.t.right(2)
