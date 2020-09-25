import turtle
pen = turtle.Pen()
pen.speed(2)
pen.pensize(5)

pen.home()


#start drawing with red pen
pen.color('red')
pen.left(135)
pen.forward(100)
pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(100)

#start drawing with blue pen
pen.color('blue')
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(100)

pen.shape('blank') #make the turtle disappear

turtle.done()

