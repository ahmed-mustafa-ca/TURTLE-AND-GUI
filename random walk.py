import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r ,g ,b)
    return random_colour


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(300):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_colour())