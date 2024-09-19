from turtle import *

speed(0)



pensize(10)







#relleno U
teleport(-200)
for i in range (-200, -150,5):
    sety(-250)
    sety(0)
    setx(i)

teleport(-150,-200)
for i in range (-150, -100,5):
    sety(-250)
    sety(-200)
    setx(i)


teleport(-100)
for i in range (-100, -50,5):
    sety(-250)
    sety(0)
    setx(i)

   

#relleno Z
teleport(0)
for i in range (0, 150,5):
    sety(-50)
    sety(0)
    setx(i)

teleport(150,-50)
for i in range (150, 75,-5):
    goto(i-75, -200)
    teleport(i,-50)
    



teleport(0,-200)
for i in range (0, 150,5):
    sety(-250)
    sety(-200)
    setx(i)


pencolor("red")
speed(5)


#U
teleport(-100,0)
forward(50)
right(90)
forward(250)
right(90)
forward(150)
right(90)
forward(250)
right(90)
forward(50)
right(90)
forward(200)
left(90)
forward(50)
left(90)
forward(200)

#Z

teleport(0)
right(90)
forward(150)
right(90)
forward(50)
right(90)
forward(150)
right(90)
forward(50)

teleport(150, -50)
goto(75, -200)
teleport(75, -50)
goto(0, -200)

teleport(0, -200)

right(90)
forward(150)
right(90)
forward(50)
right(90)
forward(150)
right(90)
forward(50)


done()