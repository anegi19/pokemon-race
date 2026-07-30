from turtle import Turtle, Screen
from random import randint, choice
from time import sleep

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Race")

#create turtle for winning message
message = Turtle()
message.hideturtle()
message.penup()
message.goto(0, -250)   # Position near the bottom of the screen

bet = screen.textinput(
    title="Place Your Bet",
    prompt="Who will win?\n(Charmander, Bulbasaur, Squirtle, Raichu or Joltik)"
)

if bet:
    bet = bet.strip().title()

#create Turtle objects
A = Turtle() 
B = Turtle()
C = Turtle()
D = Turtle()
E = Turtle()


TurtleList = [A,B,C,D,E] #list of Turtle objects
TurtleNames = ["Charmander","Bulbasaur","Squirtle","Raichu", "Joltik"] #list of Turtle names
TurtleColors = ['red','green','deepskyblue','orange', "gold"] #list of Turtle colors
TurtleStartPosX = [-160,-160,-160,-160, -160] #All Turtles start from the same X position
TurtleStartPosY = [100, 50, 0,-50, -100] # All Turtles are arranged at different Y positions at the start line

N = len(TurtleList) #number of Turtles in the race

# Assign turtle attributes
for i in range(len(TurtleList)):
    turtle = TurtleList[i]
    turtle.color(TurtleColors[i])
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-250, TurtleStartPosY[i])
    turtle.write(TurtleNames[i],
                 font=("Arial", 20, "bold"), align="right")
    turtle.pendown()

# Create finish line
finish_line = Turtle()
finish_line.penup()
finish_line.goto(350, 250)
finish_line.pendown()
finish_line.right(90)
finish_line.forward(500)
finish_line.hideturtle()

#create a turtle that counts down
countdown = Turtle()
countdown.hideturtle()
countdown.penup()
countdown.goto(0, 200)

for number in ["3", "2", "1", "GO!"]:
    countdown.clear()
    countdown.write(
        number,
        align="center",
        font=("Arial", 50, "bold")
    )
    sleep(1)

countdown.clear()



# Start race
race_on = True

while race_on:
    for turtle in TurtleList:
        turtle.forward(randint(1, 5))
        sleep(0.01)

        if turtle.xcor() >= 350:
            winner_index = TurtleList.index(turtle)
            print("The Winner is", TurtleNames[winner_index], "!")


            race_on = False
            break
    

winner = TurtleNames[winner_index]

if bet == winner:
    result = "🎉 You guessed correctly!"
else:
    result = f"❌ Womp Womp :( You bet on {bet}. 💔 "

message.clear()
message.color(TurtleColors[winner_index])

message.write(
    f"🏆 Congratulations {winner}! 🏆\n\n{result}",
    align="center",
    font=("Arial", 20, "bold")
)

# Keep window open until user closes it 
screen.mainloop()
    
    
    
