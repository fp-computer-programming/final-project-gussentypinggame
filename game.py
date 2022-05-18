# Author CCG 5/1/22

import turtle
import random

# design of the base turtle screen
screen = turtle.Screen()
screen.setup(1000,1000)
screen.title('Jesuit Typing Game')
screen.bgcolor('red')
screen.tracer(0,0)
turtle.hideturtle()
turtle.up()
turtle.color('black')
score_turtle = turtle.Turtle()
score_turtle.color('black')
score_turtle.up()
score_turtle.hideturtle()
turtle.goto(350,400)
turtle.write('Score: ', align='center', font=('Courier',25,'normal'))


# establish variables for use in the future functions
speed = 20
letters = []
pos = []
lts = []
x = 10
speeds = []
score = 0
game_over = False


def draw_score(): # function to constantly update the score
    score_turtle.clear()
    score_turtle.goto(420,400)
    score_turtle.write('{}'.format(score),align='center',font=('Courier',25,'normal'))
    screen.update()

def draw_game_over(): # function for the game over 'page'
    turtle.goto(0,0)
    turtle.color('black')
    turtle.write('GAME OVER', align='center', font=('Courier',50,'normal'))
    turtle.goto(0,-150)
    turtle.color('black')
    turtle.write('Your Score is {}'.format(score), align='center', font=('Courier',40,'normal'))
    screen.update()
    
def draw_words(): # function to draw words and to scan if the game is over
    global game_over
    for i in range(len(letters)):
        lts[i].clear()
        lts[i].goto(pos[i])
        lts[i].write(letters[i],align='center',font=('courier',20,'normal'))
        pos[i][1] -= speeds[i]
        if pos[i][1]<-500:
            game_over = True
            draw_game_over()
            return
    screen.update()
    screen.ontimer(draw_words,50)

def type(c): # function for the input of user
    global score
    if c in letters:
        score += 1
        k = letters.index(c)
        while True:
            l = chr(ord('a')+random.randrange(26))
            if l not in letters:
                letters[k] = l
                break            
        pos[k] = [random.randint(-450,450),500]        
        speeds[k] = speed
    draw_score()
        
for h in range(x): # for loop for words
    lts.append(turtle.Turtle())
    while True:
        l = chr(ord('a')+random.randrange(26))
        if l not in letters:
            letters.append(l)
            break
    speeds.append(speed)
    pos.append([random.randint(-450,450),500])
    
for i in range(x): # for loop for words
    lts[i].speed(0)
    lts[i].hideturtle()
    lts[i].up()
    lts[i].color('white')
    

draw_words() # call function


# using the previous input function in a lambda so code accepts user inputs
screen.onkey(lambda: type('a'), 'a')
screen.onkey(lambda: type('b'), 'b')
screen.onkey(lambda: type('c'), 'c')
screen.onkey(lambda: type('d'), 'd')
screen.onkey(lambda: type('e'), 'e')
screen.onkey(lambda: type('f'), 'f')
screen.onkey(lambda: type('g'), 'g')
screen.onkey(lambda: type('h'), 'h')
screen.onkey(lambda: type('i'), 'i')
screen.onkey(lambda: type('j'), 'j')
screen.onkey(lambda: type('k'), 'k')
screen.onkey(lambda: type('l'), 'l')
screen.onkey(lambda: type('m'), 'm')
screen.onkey(lambda: type('n'), 'n')
screen.onkey(lambda: type('o'), 'o')
screen.onkey(lambda: type('p'), 'p')
screen.onkey(lambda: type('q'), 'q')
screen.onkey(lambda: type('r'), 'r')
screen.onkey(lambda: type('s'), 's')
screen.onkey(lambda: type('t'), 't')
screen.onkey(lambda: type('u'), 'u')
screen.onkey(lambda: type('v'), 'v')
screen.onkey(lambda: type('w'), 'w')
screen.onkey(lambda: type('x'), 'x')
screen.onkey(lambda: type('y'), 'y')
screen.onkey(lambda: type('z'), 'z')

screen.listen()
screen.mainloop()
