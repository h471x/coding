import turtle
from turtle import *

window = Screen()
window.bgcolor('black')

t = turtle.Turtle()
t.pencolor('white')

def curve():
  for i in range(200):
    t.rt(1)
    t.fd(1)

def heart():
  t.fillcolor('red')
  t.begin_fill()
  t.lt(140)
  t.fd(113)
  curve()
  t.lt(120)
  curve()
  t.fd(112)
  t.end_fill()

heart()
t.ht()

window.mainloop()
