import turtle


def tree(branchLen, t):
    if branchLen > 5:
            t.forward(branchLen)
            t.right(20)
            tree(branchLen-15, t)
            t.left(40)
            tree(branchLen-15, t)
            t.right(20)
            t.backward(branchLen)


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


if __name__ == '__main__':
    main()
