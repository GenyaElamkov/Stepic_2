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


def square_corner(side, counter, corner) -> None:
    """Поворачивает квадрат на определнный угол."""
    for i in range(1, counter + 1):
        t.setheading(corner * i)
        square(side)
        print('Квадратов нарисовано:', i)


def hexagon_1(side) -> None:
    """Рисуем правильный шестиугольник."""
    n = 6  # Кол-во сторон
    corner = (n - 2) * 180  # Угол для многоугольника
    for i in range(n):
        t.forward(side)
        t.left(180 - corner / n)

    t.forward(side)
    t.right(180 - corner / n)


def main_hexagon_1(side):
    """Рисуем соты."""
    for i in range(1, 7):
        hexagon_1(side)


def hexagon(side) -> None:
    """Рисуем правильный шестиугольник."""
    for i in range(6):
        t.forward(side)
        t.left(60)
    t.forward(side)
    t.right(60)


def honeycombs(side) -> None:
    """Рисуем соты."""
    for i in range(1, 7):
        hexagon(side)


def rhomb(side) -> None:
    """Рисуем ромб с углами 60 и 120"""
    # t.forward(200)
    # for i in [2, 3, 5]:
    #     t.setheading(60 * i)
    #     t.forward(200)
    for i in range(4):
        t.forward(side)
        t.left(120 - 60 * (i % 2))


def rhomb_2(side) -> None:
    """Рисуем ромб в другом направлении"""
    for i in range(1, 5):
        t.forward(side)
        t.left(120 - 60 * (i % 2))


def snowflake(side, n) -> None:
    """Рисуем снежинку из n - ромбов"""
    t.speed(100)
    for i in range(1, n + 1):
        t.setheading(360 / n * i)
        rhomb_2(side)


def rays_star(side) -> None:
    """Рисуем лучи звезды, показанной на рисунке."""
    n = 30  # Кол-во лучей
    for _ in range(1, n + 1):
        t.forward(side)
        t.backward(side)
        t.left(360 / n)


def five_pointed_star(side) -> None:
    """Рисуем правильную пятиконечную звезду."""
    for i in range(5):
        t.forward(side)
        t.right(144)


def pattern_squares(side) -> None:
    """Рисуем квадрат."""
    t.penup()
    t.setx(50)
    t.pendown()
    for i in range(4):
        t.left(90)
        t.forward(side)


def set_counter_pattern_squares(side, counter) -> None:
    """Создаем узоры из квадратов."""
    t.speed(20)
    length = 0
    for i in range(1, counter):
        pattern_squares(side + length)
        length += 20


def pattern(side, counter) -> None:
    """Рисуем узор, показанный на рисунке."""
    t.speed(20)
    for i in range(1, counter + 1):
        t.left(90)
        t.forward(side * i)


def main():
    t.showturtle()
    pattern(10, 60)
    # set_counter_pattern_squares(50, 10)
    # pattern_squares()
    # five_pointed_star(200)
    # rays_star(200)
    # snowflake(200, 10)
    # rhomb_2(100)
    # honeycombs(100)
    # hexagon(100)
    # hexagon_1(100)
    # main_hexagon_1(100)
    # square_corner(200,  8, 45)
    # triangle(200)
    # rectangle(200, 100)
    t.exitonclick()


if __name__ == '__main__':
    main()
