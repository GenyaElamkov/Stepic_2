import turtle as t


def rectangle(width, height) -> None:
    """Рисуем прямоугольник"""
    t.forward(width)
    t.setheading(90)
    t.forward(height)
    t.setheading(180)
    t.forward(width)
    t.setheading(270)
    t.forward(height)


def triangle(side) -> None:
    """Правильный треугольник"""
    t.penup()
    t.setx(side / 2)
    t.pendown()
    t.setheading(120)
    t.forward(side)
    t.setheading(240)
    t.forward(side)
    t.setheading(0)
    t.forward(side)


def square(side) -> None:
    """Рисует изображенную фигуру, состоящую из трех квадратов."""
    t.speed(5)
    for i in range(4):
        t.forward(side)
        t.left(90)


def squqre_corner(side, counter) -> None:
    """Поворачивает квадрат на определнный угол."""
    for i in range(1, counter + 1):
        t.setheading(22.5 * i)
        square(side)
        print('Квадратов нарисовано:', i)


def main():
    t.showturtle()
    squqre_corner(200, 16)
    # triangle(200)
    # rectangle(200, 100)
    t.exitonclick()


if __name__ == '__main__':
    main()
