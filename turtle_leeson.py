import turtle as t
from random import choice, randint


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


def dotted_line(side):
    """Рисуем пунктирную линию"""
    size_dotted = 30
    # t.dot(5, 'red')
    t.shape('turtle')
    for _ in range(side // size_dotted):
        t.stamp()
        t.penup()
        t.forward(size_dotted)
        t.pendown()


def rectangle_dot():
    """Прямоугольник с точкой в каждом углу"""

    for i in range(1, 5):
        t.dot(10)
        side = 200
        if i % 2 == 0:
            side //= 2

        t.forward(side)
        t.left(90)


def web(n):
    """Рисуем паутину в соответствии с примером. Программа считывает количество лучей паутины, число n."""
    side = 200
    t.dot(20)
    t.pensize(2)
    for i in range(1, n + 1):
        t.forward(side)
        t.shape('triangle')
        t.stamp()
        t.backward(side)
        t.left(360 / n)


def draw_turtle(shape, side):
    """Рисуем черепашек в соответствии с образцом."""
    n = 12
    # t.shapesize(5)
    t.shape(shape)
    t.stamp()
    for i in range(1, n + 1):
        t.penup()
        t.forward(side)
        t.pendown()
        t.stamp()
        t.penup()
        t.backward(side)
        t.left(360 / n)


def watch_face():
    """Рисует циферблат часов в соответствии с образцом."""
    side = 200
    n = 12
    t.Screen().bgcolor('SkyBlue')
    t.shape('turtle')
    t.stamp()
    t.pensize(5)
    for i in range(1, n + 1):
        t.penup()
        t.forward(side - 40)
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)
        t.pendown()
        t.stamp()
        t.penup()
        t.backward(side)
        t.left(360 / n)


def turtle_spiral():
    """Рисует черепашью спираль в соответствии с образцом."""
    counter_turtle = 50
    t.Screen().bgcolor('LightGreen')
    t.shape('turtle')
    t.stamp()
    for i in range(1, counter_turtle + 1):
        t.penup()
        t.forward(2 * i)
        t.pendown()
        t.left(22)
        t.stamp()


def spiral_pattern():
    """Рисует узор в соответствии с образцом."""
    line = 5
    color = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']

    for i in range(1, 45):
        t.pencolor(choice(color))
        t.pensize(i // 3)
        t.forward(line)
        t.left(45)
        line += 2


def draw_star():
    """
    Рисует звезду, показанную на рисунке. Такую звезду можно создать из двух треугольников.
    Однако их невозможно нарисовать непрерывной линией, поэтому перо нужно будет поднять для перехода
    ко второму треугольнику.
     """
    t.speed(0)
    side = 200
    for i in range(3):
        t.forward(side)
        t.left(120)
    t.penup()
    t.goto(0, 120)
    t.pendown()
    for i in range(3):
        t.forward(side)
        t.right(120)


def draw_line():
    """Рисует изображение в соответствии с образцом."""
    n = 5
    size = 200

    temp = 0
    for _ in range(n):
        t.pencolor('red')
        t.penup()
        t.goto(0, size)
        t.pendown()
        t.dot(10)
        t.goto(size / 2 - temp, 0)
        t.pencolor('blue')
        t.dot(10)
        temp += (size / n)
        print(size)


def draw_circle():
    """Рисует изображение символа олимпиады в соответствии с образцом."""
    color = ['blue', 'black', 'red', 'yellow', 'LightGreen']
    t.pensize(5)
    counter = 0
    for i in range(2):
        for j in range(3 - i):
            t.pencolor(color[counter])
            t.circle(50)
            t.penup()
            t.forward(100)
            t.pendown()
            counter += 1
        t.penup()
        t.goto(50, -50)
        t.pendown()


def draw_bear():
    """Рисует изображение мишки в соответствии с образцом."""
    t.speed(5)
    [t.circle(50 * i) for i in range(1, 3)]
    t.penup()
    t.goto(-90, 160)
    t.pendown()
    for _ in range(1, 3):
        t.circle(25)
        t.penup()
        t.forward(180)
        t.pendown()

    t.penup()
    t.goto(-50, 100)
    t.pendown()
    for i in range(2):
        for j in range(2):
            if i == 1:
                t.penup()
                t.goto(0, 70)
                t.pendown()
                t.circle(10)
                t.right(90)
                t.forward(50)
                t.hideturtle()
                break
            else:
                t.dot(20)
                t.penup()
                t.forward(100)
                t.pendown()


def snowflakes():
    """Случайным образом рисует снежинки разного цвета и размера в соответствии с образцом."""
    t.Screen().setup(500, 500)
    t.Screen().title('Снежинки')
    t.Screen().bgcolor('cyan')

    t.speed(0)

    color = ['blue', 'indigo', 'pink', 'gray', 'gold']

    counter = 30  # Кол-во снежинок.

    for n in range(counter):
        x = randint(-200, 200)
        y = randint(-200, 200)
        t.penup()
        t.goto(x, y)
        # print(t.pos())
        t.pendown()

        # Снежинка
        side = randint(10, 50)
        segment_size = side / 4
        t.pencolor(choice(color))
        for i in range(8):
            # Рисуем сегмент
            t.forward(segment_size)
            for j in range(3):
                t.left(45)
                t.forward(segment_size)
                t.backward(segment_size)
                t.right(90)
                t.forward(segment_size)
                t.backward(segment_size)
                t.left(45)
                t.forward(segment_size)
            t.backward(side)
            t.left(360 / 8)


def main():
    t.showturtle()
    snowflakes()
    # draw_bear()
    # draw_circle()
    # draw_line()
    # draw_star()
    # spiral_pattern()
    # turtle_spiral()
    # watch_face()
    # draw_turtle()
    # web(8)
    # rectangle_dot()
    # dotted_line(200)
    # pattern(10, 60)
    # set_counter_pattern_squares(50, 10)
    # pattern_squares(200)
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
