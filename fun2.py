
import turtle
turtle.goto(0,0)

UP = 0
DOWN=1
LEFT=2
RIGHT=3
direction = None

def up():
    global direction
    direction=UP
    print("You pressed the up key.")

def down():
    global direction
    direction=DOWN
    print("You pressed the down key.")

def left():
    global direction
    direction=LEFT
    print("You pressed the left key.")
    
def right():
    global direction
    direction=RIGHT
    print("You pressed the right key.")
    


    
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.listen()

def on_move():
    print(up, down, left, right)

turtle.mainloop()


