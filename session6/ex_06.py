from math import degrees
from re import X
import turtle
leo = turtle.Turtle()

def square_length(t, length, edges, a):
    """write a function called square that takes a paramter named t, which is a turltle that will use the turltle to draw a sqaure."""
    t.setheading(a)
    for i in range(edges):
        t.fd(length)
        t.lt(360/edges)

def star_length(t, length, edges, a):
    """write a function called square that takes a paramter named t, which is a turltle that will use the turltle to draw a sqaure."""
    t.setheading(a)
    for i in range(edges):
        t.fd(length)
        t.lt(720/edges)

def draw_squares(nummber_of_squares, degreechange, length):
    for i in range(nummber_of_squares):
        square_length(leo, length, 4, i*degreechange)

def draw_shape(nummber_of_squares,degreechange,startlength,change):
    for i in range(nummber_of_squares):
        total_change=change*i
        final_change=startlength+total_change
        square_length(leo,final_change,4, i*degreechange)

#draw_squares(60,5,100)
#draw_shape(60,5,30,4)
#draw_star(leo,100,11,0)

def draw_star(nummber_of_squares,degreechange,startlength,change):
    for i in range(nummber_of_squares):
        total_change=change*i
        final_change=startlength+total_change
        star_length(leo,final_change,5, i*degreechange)
#draw_star(leo,100,11,0)
draw_star(60,5,30,4)
