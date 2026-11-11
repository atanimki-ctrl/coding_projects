import turtle

turtle.bgcolor("midnight blue")
turtle.title("My Drawing")
turtle.speed("fastest")
turtle.width(2)

def make_flower(radius, shade):
    turtle.color(shade)
    turtle.begin_fill()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.end_fill()

flower_colours = ["hotpink", "violet", "turquoise", "gold", "coral", "magenta", "lightgreen", "skyblue"]

for petal in range(36):
    make_flower(100, flower_colours[petal % len(flower_colours)])
    turtle.right(10)

turtle.penup()
turtle.goto(0, -20)
turtle.pendown()

turtle.color("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.done()
