"""Turtle project !!!"""
 
__author__ = "730470758"

import turtle
import random


def draw_star(turtle_obj: turtle.Turtle, x: float, y: float, size: int, color: str = "white") -> None:
    """This function attempts to create a single five point star."""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    for i in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(144)
    turtle_obj.end_fill()


def draw_starry_night(turtle_obj: turtle.Turtle, num_stars: int) -> None:
    """This function utilizes a for loop.

    the loop calls the draw_star function above.
    And places a given number of stars randomly around the screen.
    """
    for i in range(num_stars):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(1, 4)
        draw_star(turtle_obj, x, y, size)


def draw_moon(turtle_obj: turtle.Turtle, x: float, y: float, radius: int) -> None:
    """Function used to draw moon in corner of screen."""
    turtle_obj.penup()
    turtle_obj.goto(x, y - radius)
    turtle_obj.pendown()
    turtle_obj.color("light gray")
    turtle_obj.begin_fill()
    turtle_obj.circle(radius)
    turtle_obj.end_fill()


def draw_sun(turtle_obj: turtle.Turtle, x: float, y: float, radius: int) -> None:
    """Function used to draw sun in corner of screen."""
    turtle_obj.penup()
    turtle_obj.goto(x, y - radius)
    turtle_obj.pendown()
    turtle_obj.color("yellow")
    turtle_obj.begin_fill()
    turtle_obj.circle(radius)
    turtle_obj.end_fill()


def draw_trunk(turtle_obj: turtle.Turtle, x: float, y: float, size: int) -> None:
    """Function used to draw trunk of tree."""
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("brown")
    turtle_obj.begin_fill()
    turtle_obj.setheading(90)
    turtle_obj.forward(size * 2)
    turtle_obj.right(90)
    turtle_obj.forward(size / 2)
    turtle_obj.right(90)
    turtle_obj.forward(size * 5)
    turtle_obj.end_fill()


def draw_leaves(turtle_obj: turtle.Turtle, x: float, y: float, size: int, level: int) -> None:
    """Function used to draw leaves of tree."""
    if level == 0:
        return None
    else:
        turtle_obj.color("green")
        turtle_obj.width(level + 100)
        turtle_obj.penup()
        turtle_obj.goto(int(x), int(y) + 150)
        turtle_obj.pendown()
        turtle_obj.setheading(60)
        turtle_obj.forward(int(size) + 50)
        draw_leaves(turtle_obj, turtle_obj.xcor() - 40, turtle_obj.ycor() - 250, int(size * 0.8), level - 1)


def draw_tree(turtle_obj: turtle.Turtle, x: float, y: float, size: int, level: int) -> None:
    """Calling trunk and branch functions to create full tree."""
    """
    Prior to breaking up, the tree function was my most complex function.
    So I decided to break it up into a function that creates the leaves for the tree.
    and made another function that creates the trunk of the tree.
    """
    draw_trunk(turtle_obj, x, y, size)
    draw_leaves(turtle_obj, x, y + size / 2, int(size / 2), level)


def draw_shooting_star(turtle_obj: turtle.Turtle, x: float, y: float, length: int) -> None:
    """For this function I attempt to draw a shooting star.

    I utilize the .stamp function for turtle objects to create a stamped impression
    on the Turtle so that I could create the shooting star. The function
    is leaving a visual mark on the canvas at the current position
    of the turtle without drawing a line as it moves. This is supposed to simulate
    the movement of a shooting star.
    """
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


def draw_star_trail(turtle_obj: turtle.Turtle, x: float, y: float, num_stars: int, max_size: int) -> None:
    """Function attempting to add a trail to shooting stars."""
    """
    
    I wanted to add more detail to my shooting stars so I decided to 
    create a function that iterates num_stars times to draw multiple 
    lines that simulates the trail seen behind shooting stars.
    """
    for i in range(num_stars):
        size = random.randint(1, max_size)
        color = random.choice(["white", "yellow", "light yellow"])
        draw_star(turtle_obj, x, y, size * 2, color)


def main() -> None:
    """Main function."""
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    turtle.speed(0)
    turtle.tracer(0, 0)
    pen = turtle.Turtle()
    """

    The below code starts by using the draw_starry_night function
    to draw 100 stars randomly on the screen. I also use the draw_moon
    function to draw a moon in the top left corner of screen. and
    used the draw_sun functiion to draw a sun in the top right corner of 
    the screen to create an image of the beginning of a reverse eclipse, 
    where the sun is in front of the moon at night.
    """
    draw_starry_night(pen, 100)
    draw_moon(pen, -300, 200, 50)
    draw_sun(pen, 300, 200, 50)
    # The below for loop is drawing 50 additional stars randomly on the screen for more detail.
    for j in range(50):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(1, 4)
        draw_star(pen, x, y, size)
    pen.color("brown")
    draw_tree(pen, 0, -300, 150, 6)
    # The below for loop is drawing 5 shooting stars randomly on the screen
    for k in range(5):
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