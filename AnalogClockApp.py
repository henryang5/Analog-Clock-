# Henry Ang
# 3/9/17
# CSC 4800
# Lab 8: Analog Clock
# Application draws a 12 hour analog clock using Python Tkinter library

from tkinter import *
from datetime import *
from math import *

def createClock(canvas):
    """
    Draws clock for application on canvas
    :param canvas:
    """
    canvasHeight = 600  # x
    canvasWidth = 600   # y
    clockRadius = 200
    dotRadius = 10

    xCenter = canvasHeight / 2
    yCenter = canvasWidth / 2

    rHourNum = 1.2 * clockRadius
    rSecNum =  0.9 * clockRadius
    rHourHand = 0.5 * clockRadius   # Hour hand 50 % clock radius
    rMinHand = 0.75 * clockRadius   # Minute hand 75 % clock radius
    rSecHand = 0.75 * clockRadius   # Second hand 75 % clock radius

    # draw outline of clock
    canvas.create_oval((xCenter - clockRadius),(yCenter - clockRadius),
                       (xCenter + clockRadius),(yCenter + clockRadius), width = 3)

    # draw dot in middle of clock
    canvas.create_oval((xCenter - dotRadius),(yCenter - dotRadius),
                       (xCenter + dotRadius),(yCenter + dotRadius), fill="black")

    # draw hours numbers
    for i in range(1, 13):                                     # 1 - 12
        angleHour = (pi / 6) * i                               # angle of each hour
        xHourNum = xCenter + (rHourNum * sin(angleHour))       # position of each hour
        yHourNum = yCenter - (rHourNum * cos(angleHour))
        canvas.create_text(xHourNum, yHourNum, text=str(i), font=('Times', '56'))

    # draw seconds
    for i in range(0, 60):                             # 0 - 60
        angleSec = (pi / 30) * i                       # angle of each second
        xSecNum = xCenter + (rSecNum * sin(angleSec))  # position of each second
        ySecNum = yCenter - (rSecNum * cos(angleSec))
        if (i % 5 == 0):                               # every 5 sec draw num
            canvas.create_text(xSecNum, ySecNum, text = i, font=('Times', '8'))
        else:                                          # draw dot
            canvas.create_text(xSecNum, ySecNum, text = " • ", font=('Times', '8'))

    # get hour, minutes, seconds
    hour = datetime.now().hour
    mintues = datetime.now().minute
    seconds = datetime.now().second

    #draw hour hand
    angleHour = (pi / 6) * hour                         # angle of each hour
    xHourHand = xCenter + (rHourHand * sin(angleHour))  # position of each hour
    yHourHand = yCenter - (rHourHand * cos(angleHour))
    canvas.create_line(xCenter, yCenter, xHourHand, yHourHand, width = 7, fill="black")

    # draw minute hands
    angleMinute = (pi / 30) * mintues
    xMinHand = xCenter + (rMinHand * sin(angleMinute))
    yMinHand = yCenter - (rMinHand * cos(angleMinute))
    canvas.create_line(xCenter, yCenter, xMinHand, yMinHand, width = 4, fill="blue")

    # draw seconds hands
    angleSecond = (pi / 30) * seconds
    xSecHand = xCenter + (rSecHand * sin(angleSecond))
    ySecHand = yCenter - (rSecHand * cos(angleSecond))
    canvas.create_line(xCenter, yCenter, xSecHand, ySecHand, width = 2, fill="red")

    canvas.pack()

root = Tk()

# create title of program
root.title("Clock Tkinter App")

# create title label
label = Label(root, text='Henry\'s Analog Clock')
label.pack()

# create canvas
canvas = Canvas(root, height = 600, width = 600)  # bg="lightgray"

def timeUpdate():
    """
    Delete previous canvas and update clock every 500 ms.
    """
    canvas.delete(ALL)
    createClock(canvas)
    root.after(500, timeUpdate)

root.after(500, timeUpdate)

mainloop()