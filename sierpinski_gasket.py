from turtle import *


def fractal(count, length):
    if count<=0:
        return
    forward(length)
    left(120)
    fractal(count-1, length/2)
    right(120)
    fractal(count-1, length/2)
    right(120)
    fractal(count-1, length/2)
    left(120)
    forward(length)


count = 7
length = ((window_width()/2-100)//2**count)*2**count

speed(0)
up()
setpos(-length, -length)
down()

input('Start')

fractal(count, length)

for _ in range(2):
    left(120)
    forward(length*2)

input('Press Enter')
