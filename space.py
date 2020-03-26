import turtle
import os
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#create invaders

enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2                                      #setting the pixel

#create the player's bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move player to left and right

def move_left():
    x = player.xcor()
    x-= playerspeed          #x=-15
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x+= playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move bullet just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet, "space")


#main game loop
while True:
    
    #move the enemy
    x = enemy.xcor()
    x+= enemyspeed
    enemy.setx(x)

    #move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y-= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    #move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y) 

    #check to see if bullet is gont to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    #check for collision btw bullet and enemy
    if isCollision(bullet, enemy):
        #reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        #reset the enemy
        enemy.setposition(-200,250)


delay = input("press enter to finish")