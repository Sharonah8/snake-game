from turtle import *
from random import randrange
from freegames import square,vector

food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0,-10)

# declare the functions in the game
#change function with 2 parameters: x,y
def change(x,y):
#x-axis and y-axis
    aim.x=x
    aim.y=y

#define function
def inside(head):
#boundary values. If the snake crosses these boundaries, game's over.
    return -200 < head.x <190 and -200 < head.y < 190

#move function. Gives movement to our snake.
def move():
#forward movement
    head=snake[-1].copy()
    head.move(aim)

#conditions
#1st condition: if the head hits the boundary, or reaches its body, game over
    if not inside(head) or head in snake:
        square(head.x,head.y,9,'red')
        update()
        return

#add the red box when snake collides
    snake.append()

#if the snake's head meets food, print out the points scored
    if head==food:
        print('snake',len(snake))
#next position where the food will appear
        food.x=randrange(-15,15)*10
        food.y=randrange(-15,15)*10
    
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x,body.y,9,'green')

    square(food.x,food.y,9,'red')
    update()
    ontimer(move, 100)

    hideturtle()
#tracer object brings back an element into its initial state
    tracer(False)
#listen object continuously updates the game each second
    listen()
#give controls to our keys and give them graph values in x- and y- axis
    onkey(lambda:changes(10,0),'Right')
    onkey(lambda:changes(10,0),'Left')
    onkey(lambda:changes(10,0),'Up')
    onkey(lambda:changes(10,0),'Down')

    move()
    done()
    