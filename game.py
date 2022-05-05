# Author CCG 5/4/22

import turtle
import random

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title('Jesuits Typing Game')
screen.bgcolor('black')
screen.tracer(0,0)
turtle.hideturtle()
turtle.up()
turtle.color('red')
score_turtle = turtle.Turtle()
score_turtle.color('red')
score_turtle.up()
score_turtle.hideturtle()
turtle.goto(350,400)
turtle.write('Score: ', align='center', font=('Courier',25,'bold'))

