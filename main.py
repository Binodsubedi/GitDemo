import turtle


move = turtle.Turtle()
move.speed(1)
Ant = 20
Elephant = 30
def moving():
 move.forward(100)
 move.left(90)
 move.forward(100)
 move.left(90)
 move.forward(100)
 move.left(90)
 move.forward(100)


while Elephant > Ant:
    moving()


