import turtle as c

c.color('black')
c.width(2)
c.penup()
c.goto(0,-150)

c.pendown()
c.fillcolor('#AA1428')
c.begin_fill()
c.circle(150)
c.end_fill()

c.width(1)
c.color('#AA1428')
c.penup()
c.goto(0,-120)
c.pendown()
c.fillcolor('white')
c.begin_fill()
c.circle(120)
c.end_fill()

c.color('#AA1428')
c.penup()
c.goto(0,-90)
c.pendown()
c.fillcolor('#AA1428')
c.begin_fill()
c.circle(90)
c.end_fill()

c.color('#AA1428')
c.penup()
c.goto(0,-60)
c.pendown()
c.fillcolor('#000042')
c.begin_fill()
c.circle(60)
c.end_fill()

c.hideturtle()

c.color('white')
c.penup()
c.goto(0,60)
c.pendown()
c.fillcolor('white')
c.begin_fill()
c.left(72)
for i in range(5):
    c.right(144)
    c.forward(111)
c.end_fill()

c.done()

