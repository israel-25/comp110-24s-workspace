"""Turtle project !!!"""
 
__author__ = "730470758"


import turtle
import random

def draw_star(turtle_obj, x, y, size, color="white"):
    """Function used to draw a star."""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(144)
    turtle_obj.end_fill()

def draw_starry_night(turtle_obj, num_stars):
    """Function used to draw multiple stars."""
    for _ in range(num_stars):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(1, 4)
        draw_star(turtle_obj, x, y, size)

def draw_moon(turtle_obj, x, y, radius):
    """Function used to draw moon in corner of screen."""
    turtle_obj.penup()
    turtle_obj.goto(x, y - radius)
    turtle_obj.pendown()
    turtle_obj.color("light gray")
    turtle_obj.begin_fill()
    turtle_obj.circle(radius)
    turtle_obj.end_fill()

def draw_trunk(turtle_obj, x, y, size):
    """Function used to draw trunk of tree."""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("brown")
    turtle_obj.begin_fill()
    turtle_obj.setheading(90)
    turtle_obj.forward(size)
    turtle_obj.right(90)
    turtle_obj.forward(size / 2)
    turtle_obj.right(90)
    turtle_obj.forward(size)
    turtle_obj.end_fill()

def draw_branches(turtle_obj, x, y, size, level):
    """Function used to draw branches of tree."""
    if level == 0:
        return
    else:
        turtle_obj.color("green")
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()
        turtle_obj.setheading(60)
        turtle_obj.forward(size)
        draw_branches(turtle_obj, turtle_obj.xcor(), turtle_obj.ycor(), size * 0.7, level - 1)
        turtle_obj.backward(size)
        turtle_obj.setheading(120)
        turtle_obj.forward(size)
        draw_branches(turtle_obj, turtle_obj.xcor(), turtle_obj.ycor(), size * 0.7, level - 1)
        turtle_obj.backward(size)

def draw_tree(turtle_obj, x, y, size, level):
    """Function calling trunk and branch functions to create full tree."""
    draw_trunk(turtle_obj, x, y, size)
    draw_branches(turtle_obj, x, y + size / 2, size / 2, level)

def draw_shooting_star(turtle_obj, x, y, length):
    """Function attempting to draw shooting star"""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("yellow")
    turtle_obj.width(3)
    turtle_obj.setheading(60)
    turtle_obj.forward(length)
    turtle_obj.stamp()
    turtle_obj.backward(length)
    turtle_obj.setheading(-60)
    turtle_obj.forward(length)
    turtle_obj.stamp()

def draw_star_trail(turtle_obj, x, y, num_stars, max_size):
    """Function attempting to add a trail to shooting stars"""
    for _ in range(num_stars):
        size = random.randint(1, max_size)
        color = random.choice(["white", "yellow", "light yellow"])
        draw_star(turtle_obj, x, y, size, color)

def main():
    """Main function."""
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    turtle.speed(0)  

    turtle.tracer(0, 0)
    pen = turtle.Turtle()
    draw_starry_night(pen, 100)
    draw_moon(pen, -300, 200, 50)
    for _ in range(50):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(1, 4)
        draw_star(pen, x, y, size)
    pen.color("brown")
    draw_tree(pen, 0, -300, 150, 6)
    for _ in range(5):
        x = random.randint(-400, 400)
        y = random.randint(-200, 300)
        length = random.randint(50, 150)
        draw_shooting_star(pen, x, y, length)
        draw_star_trail(pen, x, y, 5, 5)
    turtle.update()
    pen.hideturtle()
    turtle.done()
if __name__ == "__main__":
    main()


