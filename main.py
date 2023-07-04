from turtle import *

#we want to paint a house

#step 1: draw a square

width(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("purple")
left(30)
forward(200)
left(90)
forward(130)
left(90)
color("brown")
forward(60)
left(90)
color("black")
forward(20)


exitonclick()
