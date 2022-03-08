import turtle
import math
########### Your Code here ##############
def setupWindow(wn):
  wn = turtle.Screen()
  wn.setworldcoordinates(-360,-1,360,1)
  wn.bgcolor("red")

def setupAxis(num):
  num = turtle.Turtle()
  num.hideturtle()
  num.penup()
  num.goto(0,-1.5)
  num.pendown()
  num.goto(0,1.5)
  num.penup()
  num.goto(-400,0)
  num.pendown()
  num.goto(400,0)

def drawSineCurve(num):
  num = turtle.Turtle()
  num.hideturtle()
  num.speed(2)
  num.width(2)
  num.penup()
  num.goto(-360,0)
  for x in range (-360,361):
    num.pendown()
    y = (math.sin(math.radians(x)))
    num.goto(x,y)
  num.clear()

def drawCosineCurve(num):
  num = turtle.Turtle()
  num.hideturtle()
  num.speed(2)
  num.width(2)
  num.penup()
  num.goto(-360,361)
  for x in range (-360,361):
    num.pendown()
    y = (math.cos(math.radians(x)))
    num.goto(x,y)
  num.clear()

def drawTangentCurve(num):
  num = turtle.Turtle()
  num.hideturtle()
  num.speed(2)
  num.width(2)
  num.penup()
  num.goto(-360,0)
  for x in range (-360,361):
    num.pendown()
    y = (math.tan(math.radians(x)))
    num.goto(x,y)
  num.clear()




  
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    num = turtle.Turtle()
    num.speed(0)
    drawSineCurve(num)

    #Part B
    setupWindow(wn)
    setupAxis(num)
    num.speed(0)
    drawSineCurve(num)
    drawCosineCurve(num)
    drawTangentCurve(num)
    wn.exitonclick()
main()
