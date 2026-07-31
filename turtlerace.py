from turtle import Turtle, Screen
from random import randint, choice
import time
from time import sleep

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pokemon Race")
screen.bgpic("bkg.gif")
screen.addshape("rsz_charmander.gif")
screen.addshape("rsz_bulbasaur.gif")
screen.addshape("rsz_squirtle.gif")
screen.addshape("rsz_raichu.gif")
screen.addshape("rsz_joltik.gif")


for i in range(1, 5):
    frame = f"puddle_{i}.gif"
    screen.addshape(frame)
    
for i in range(1, 4):
    frame = f"rsz_berries_{i}.gif"
    screen.addshape(frame)

# Create cheering Pikachu at finish line
pikachu_frames = []
for i in range(1, 24):
    frame = f"pikachu_gif_split/frame_{i:02d}.gif"
    screen.addshape(frame)
    pikachu_frames.append(frame)

pikachu_frame = 0

def animate_pikachu():
    global pikachu_frame

    pikachu.shape(pikachu_frames[pikachu_frame])

    pikachu_frame += 1

    if pikachu_frame >= len(pikachu_frames):
        pikachu_frame = 0

    screen.ontimer(animate_pikachu, 10)

def pikachu_says(text):
    pikachu_chat.clear()

    pikachu_chat.goto(150, 250)

    pikachu_chat.write(
        "💬 " + text,
        align="center",
        font=("Arial", 20, "bold")
    )

    #screen.ontimer(pikachu_chat.clear, 3000)

#create turtle for winning message
message = Turtle()
message.hideturtle()
message.penup()
message.goto(0, -250)   # Position near the bottom of the screen


# random messages for each puddle/boost
puddle_messages = [
    "{} slipped in the mud!",
    "{} got splashed!",
    "{} lost their footing!",
    "{} stepped into a puddle!",
    "{} is covered in mud!",
    "{} was slowed by a puddle!",
    "{} got stuck in the muck!",
    "Splash! {} is soaked!",
    "{} can't catch a break!",
    "A wild puddle appeared! {} was hit!"
]

berry_messages = [
    "{} found a tasty Berry!",
    "{} got a speed boost!",
    "{} is charging ahead!",
    "{} feels energized!",
    "{} found a hidden Berry!",
    "{} ate an Oran Berry!",
    "{} is full of energy!",
    "Critical speed boost for {}!",
    "{} is moving at lightning speed!",
    "It's super effective! {} sped up!"
]



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
TurtleShapes = ['rsz_charmander.gif', 'rsz_bulbasaur.gif', 'rsz_squirtle.gif', 'rsz_raichu.gif', 'rsz_joltik.gif'] #list of Turtle shapes
#TurtleStartPosX = [-160,-160,-160,-160, -160] #All Turtles start from the same X position
TurtleStartPosY = [140, 70, 0, -70, -140] # All Turtles are arranged at different Y positions at the start line

N = len(TurtleList) #number of Turtles in the race

# Assign turtle attributes
for i in range(len(TurtleList)):
    turtle = TurtleList[i]
    turtle.color(TurtleColors[i])
    turtle.shape(TurtleShapes[i])
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

# Create cheering Pikachu at finish line
pikachu = Turtle()
pikachu.penup()
pikachu.goto(300, 220) # near finish line

# Pikachu speech bubble
pikachu_chat = Turtle()
pikachu_chat.hideturtle()
pikachu_chat.penup()
pikachu_chat.goto(0, 300)

animate_pikachu()


# Start race
race_on = True
screen.tracer(0)

while race_on:

    for i, turtle in enumerate(TurtleList):
        turtle.forward(randint(1, 5))
        
        flag = True
        if randint(1,1000) < 5: #create hurdle
            x_ = turtle.xcor()
            y_ = turtle.ycor()
            puddle = Turtle()
            shape_num = randint(1,4)
            puddle.shape(f"puddle_{shape_num}.gif")    
            puddle.penup()
            puddle.goto(x_, y_)
            puddle.backward(30)

            pikachu_says(
                "🫠" + choice(puddle_messages).format(TurtleNames[i]),
            )
            flag = False
            sleep(0.04)

        if randint(0,1000) <= 1 and flag: #create boost
            x_ = turtle.xcor()
            y_ = turtle.ycor()
            boost = Turtle()
            shape_num = randint(1,3)
            boost.shape(f"rsz_berries_{shape_num}.gif")    
            boost.penup()
            boost.goto(x_, y_)
            turtle.forward(40)
            pikachu_says(
                "⚡" + choice(berry_messages).format(TurtleNames[i])
            )
            sleep(0.04)

        if turtle.xcor() >= 350:
            winner_index = TurtleList.index(turtle)
            print("The Winner is", TurtleNames[winner_index], "!")
            race_on = False
            break
    sleep(0.08)
    screen.update()
     
    

winner = TurtleNames[winner_index]

if bet == winner:
    result = "---🎉 You guessed correctly!---"
else:
    result = f"--- Womp Womp 👎 You bet on {bet}.---"

pikachu_chat.clear()
message.clear()
message.color(TurtleColors[winner_index])

message.write(
    f"🏆 Congratulations {winner}! 🏆\n\n{result}",
    align="center",
    font=("Arial", 20, "bold")
)

# Keep window open until user closes it 
screen.mainloop()
    
    
    
