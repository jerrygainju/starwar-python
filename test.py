import turtle
import os
import math
import random
import winsound
import platform 




wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invader ")
wn.bgpic("space_invaders_background.gif")
wn.tracer(0)


#register the shape
wn.register_shape("invader.gif")
wn.register_shape("player.gif")


#create border turlte
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

#create score board
score = 0

#create turtle for score pen
score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.speed(0)
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: {}" .format(score)
score_pen.write(scorestring, False, align ="left", font=("Ariel",14,"normal"))
score_pen.hideturtle()


#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.setposition(0,-250)
player.setheading(90)
player.speed = 0


#choose enemy number
number_of_enemies = 40
#create empty list of enemies
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    #create enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225 
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif") 
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50* enemy_number)
    y = enemy_start_y 
    enemy.setposition(x,y)
    #update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.18



#create playres bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bullet.speed = 5

#bullet state
#ready to fire
#bullet is firing
bulletstate = "ready"

#move player left and right using function
def move_left():
    player.speed = -1
    
 
def move_right():
    player.speed = 1

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > +280:
        x = +280
    player.setx(x)


def fire_bullet():
    #declare bullet state as as global if it need to change
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        #move bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



#giving command to keyboard left right keys by calling function
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(fire_bullet,"space")




#main gameloop
while True:
    wn.update()
    move_player()
    for enemy in enemies:
    #move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        #move the enemy back and down
        if enemy.xcor() > 280:
            #moves all enemy down
            for e in enemies:
                y = e.ycor() 
                y -= 40
                e.sety(y)
                #change direction
            enemyspeed *= -1    

        if enemy.xcor() < -280:
            #moves all enemy down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                #change direction
            enemyspeed *= -1

        #check for colision between bullet and enemy
        if isCollision(bullet,enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            #reset bullets
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            #reset enemy postiion
            enemy.setposition(0,1000)
            #update score
            score += 10
            scorestring = "Score: {}" .format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align ="left", font=("Ariel",14,"normal"))


        if isCollision(player,enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break

        #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bullet.speed
        bullet.sety(y)

        #check to see if the billet has gone to the top
    if bullet.ycor() > 270:
        bullet.hideturtle()
        bulletstate = "ready"



        
        




