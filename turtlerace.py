from turtle import Turtle
from random import randint


#create Turtle objects
lars = Turtle() 
anjali = Turtle()
kai = Turtle()
sven = Turtle()
leon = Turtle()

TurtleList = [A,B,C,D,E] #list of Turtle objects
TurtleNames = ["Charmander","Bulbasaur","Squirtle","Raichu", "Joltik"] #list of Turtle names
TurtleColors = ['red','green','blue','orange', "yellow"] #list of Turtle colors
TurtleStartPosX = [-160,-160,-160,-160, -160] #All Turtles start from the same X position
TurtleStartPosY = [100,50,0,-50, -100] # All Turtles are arranged at different Y positions at the start line

N = len(TurtleList) #number of Turtles in the race

#assign attributes to the Turtles
for i in range(N):
    turtle = TurtleList[i]
    turtle.color(TurtleColors[i])
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(TurtleStartPosX[i],TurtleStartPosY[i])
    turtle.pendown()


#Start the Race!
for movement in range(100):
    for turtle in TurtleList:
        turtle.forward(randint(1,5))
    


TurtleEndPosX =[] #To store the End positions of the Turtles
 
for turtle in TurtleList:
    TurtleEndPosX.append(turtle.xcor())


#Find and declare the turtle that ran the most distance as the winner 
max_index = TurtleEndPosX.index(max(TurtleEndPosX)) 

print("The Winner is", TurtleNames[max_index], "!")


#To prevent the IDE from closing the program instantly
input("Press Enter to close")
    
    
    
