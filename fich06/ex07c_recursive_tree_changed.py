import turtle
import random


def tree(branch_len, t):
    if branch_len > 5:
        if branch_len >= 12:
            t.pensize(3)
            t.color("brown")
        else:
            t.pensize(1.5)
            t.color("green")
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - random.randint(5, 15), t)
        t.left(40)
        tree(branch_len - random.randint(5, 15), t)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, t)
    my_win.exitonclick()


main()
