import turtle as turtle_module
import random
#import colorgram
# rgbColors = []
# colors = colorgram.extract("hirst.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r,g,b)
#     rgbColors.append(new_color)
#print(rgbColors)
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(235, 228, 210), (60, 104, 143), (216, 151, 81), (128, 91, 61), (238, 225, 234), (221, 201, 117), (145, 176, 198), (191, 144, 169), (140, 76, 99), (208, 92, 65), (69, 109, 89), (134, 178, 137), (185, 84, 113), (43, 156, 185), (70, 154, 94), (148, 133, 77), (14, 50, 87), (183, 191, 203), (30, 64, 111), (64, 50, 39), (215, 178, 196), (123, 39, 49), (116, 119, 150), (170, 207, 185), (44, 61, 56), (79, 36, 50), (233, 173, 164), (162, 208, 215)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()