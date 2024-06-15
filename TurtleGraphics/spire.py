from turtle import Turtle,Screen
import random
timmy = Turtle()
colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","seagreen",]
direction = [0,90,180,270]
#timmy.pensize(15)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random.choice(colours))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
draw_spirograph(5)

# for _ in range(200):
#     timmy.color(random.choice(colours))
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(200):
#         timmy.forward(30)
#         timmy.right(angle)
# for shape_side_n in range(3,11):
#       timmy.color(random.choice(colours)
#       draw_shape(shape_side_n)
screen = Screen()
screen.exitonclick()