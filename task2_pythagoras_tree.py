import math
import turtle

def draw_branch(t: turtle.Turtle, length: float, level: int) -> None:
    if level == 0:
        return

    t.forward(length)
    t.left(45)
    draw_branch(t, length / math.sqrt(2), level - 1)
    t.right(90)
    draw_branch(t, length / math.sqrt(2), level - 1)
    t.left(45)
    t.backward(length)

def draw_pythagoras_tree(level: int) -> None:
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    draw_branch(t, 120, level)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    try:
        recursion_level = int(input("Enter recursion level, for example 6-10: "))
        if recursion_level < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non-negative integer.")
    else:
        draw_pythagoras_tree(recursion_level)
