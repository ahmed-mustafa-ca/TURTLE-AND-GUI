import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [ (209, 166, 126), (140, 49, 106), (164, 169, 38), (244, 80, 57), (232, 112, 163), (214, 232, 229), (2, 142, 50), (241, 65, 139), (1, 143, 184), (53, 202, 225), (162, 56, 52), (20, 165, 125), (254, 230, 0), (242, 222, 56), (163, 188, 174), (28, 196, 219), (228, 167, 192)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1 , number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen= turtle_module.Screen()
screen.exitonclick()