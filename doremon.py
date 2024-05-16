import turtle

# yha per user turtle ka setup krega
t = turtle.Turtle()
t.speed(3)

# yha per doremon ka face banega
t.fillcolor("#03A9F4")
t.begin_fill()
t.circle(100)
t.end_fill()

# yha per doremon ka aankh banega
t.penup()
t.goto(-40, 120)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-40, 130)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40, 120)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(40, 130)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(10)
t.end_fill()

# yha per doremon ka nose banega
t.penup()
t.goto(0, 80)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# yha per doremon ka mouth banega
t.penup()
t.goto(-40, 40)
t.pendown()
t.setheading(-30)
t.width(5)
t.circle(40, 120)

# yha per doremon ka munch banega
t.penup()
t.goto(-60, 60)
t.pendown()
t.setheading(60)
t.forward(120)

t.penup()
t.goto(-60, 40)
t.pendown()
t.setheading(120)
t.forward(120)

t.penup()
t.goto(-60, 20)
t.pendown()
t.setheading(60)
t.forward(120)

t.penup()
t.goto(60, 60)
t.pendown()
t.setheading(120)
t.forward(120)

t.penup()
t.goto(60, 40)
t.pendown()
t.setheading(60)
t.forward(120)

t.penup()
t.goto(60, 20)
t.pendown()
t.setheading(120)
t.forward(120)

# Hide the turtle
t.hideturtle()