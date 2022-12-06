import turtle as t
from random import choice, randint, randrange
from math import radians, tan


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


def draw_home():
    """Рисует изображение домика по образцу."""

    side = 200
    tim_1, tim_2 = [t.Turtle() for _ in range(2)]
    tim_1.hideturtle()
    tim_2.hideturtle()

    def draw_tingle(tim_1, side):
        tim_1.fillcolor('black')
        tim_1.begin_fill()
        for i in range(4):
            if i == 0 or i == 3:
                tim_1.forward(side / 2)
            else:
                tim_1.forward(side)
            tim_1.left(120)
        tim_1.end_fill()

    def draw_squre(tim_2, side):

        tim_2.fillcolor('yellow')
        tim_2.begin_fill()
        tim_2.penup()
        tim_2.goto((side / 2) - 20, 0)
        tim_2.pendown()

        for i in range(3):
            tim_2.right(90)
            if i == 1:
                tim_2.forward(side - 40)
            else:
                tim_2.forward(side - 60)
        tim_2.end_fill()

    draw_tingle(tim_1, side)
    draw_squre(tim_2, side)


def draw_rectangle_traffic_lights():
    """Рисуем прямоугольник."""
    rectangle = t.Turtle()
    rectangle.hideturtle()
    rectangle.speed(5)
    rectangle.fillcolor('black')
    rectangle.begin_fill()
    for i in range(4):
        if i == 1 or i == 3:
            rectangle.forward(300)
        else:
            rectangle.forward(100)
        rectangle.left(90)
    rectangle.end_fill()


def draw_circle_traffic_lights(turtles):
    """Рисуем круг."""
    head = 30
    for turtle in turtles:
        turtle.penup()
        turtle.goto(50, head)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        head += 90


def traffic_lights():
    """Рисует изображение светофора по образцу."""
    draw_rectangle_traffic_lights()

    color = ['green', 'yellow', 'red']

    turtles = []
    for i in range(3):
        turt = t.Turtle()
        turt.speed(0)
        turt.hideturtle()
        turt.pencolor(color[i])
        turt.fillcolor(color[i])
        turt.pensize(3)
        turtles.append(turt)

    draw_circle_traffic_lights(turtles)


def optical_illusion():
    """Рисует оптическую иллюзию по образцу."""

    t.Screen().bgcolor('white')

    for _ in range(3):
        t.forward(120)
        t.left(120)

    t.penup()
    t.goto(0, 80)
    t.fillcolor('white')
    t.pencolor('white')
    t.begin_fill()

    for _ in range(3):
        t.dot(30, 'black')
        t.forward(120)
        t.right(120)

    t.end_fill()


"""    
    import turtle
    turtle.speed(5)
    
    for _ in range(3):
        turtle.forward(90)
        turtle.left(120)
    
    turtle.penup()
    turtle.goto(0, 60)
    
    turtle.color('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(90)
        turtle.color('black')
        turtle.dot(30)
        turtle.color('white')
        turtle.right(120)
    
    turtle.end_fill()
"""


def draws_rainbow_image():
    t.Screen().colormode(255)
    t.tracer(25, 0)
    circ = t.Turtle()
    circ.hideturtle()
    circ.speed(0)

    for i in range(0, 201, 20):
        circ.penup()
        circ.goto(0, -200 + i)
        circ.pendown()
        circ.color(randrange(256), randrange(256), randrange(256))
        circ.begin_fill()
        circ.pencolor('black')
        circ.circle(200 - i)
        circ.end_fill()


def draws_image_crescent_moon():
    """Рисует изображение полумесяца."""
    t.Screen().bgcolor('blue')
    t.speed(0)
    t.tracer(25, 0)
    color = ['yellow', 'blue']
    for i in range(0, 51, 50):
        t.goto(0 + i, -100)
        t.color(color[i // 50])
        t.begin_fill()
        t.circle(200)
        t.end_fill()


def animated_image_phases_moon():
    """Рисует анимированное изображение фаз луны."""
    t.hideturtle()
    t.Screen().bgcolor('blue')
    t.dot(200, 'orange')
    moon = t.Turtle()
    moon.hideturtle()
    # moon.tracer(25, 0)
    moon.up()
    for i in range(200, -201, -1):
        moon.goto(i, 0)
        moon.clear()
        moon.dot(200, 'blue')


def test():
    t.Screen().setup(500, 500)
    t.Screen().bgcolor('grey')
    text = t.textinput(title='Вопрос', prompt='Ваше имя:')
    num = t.numinput(title='Вопрос', prompt='Ваш возраст:')
    print(text, num)


def set_stars():
    """
    Рисует изображение по образцу. Звезды должны быть рассыпаны случайно,
    иметь разный размер и цвет.
    """
    t.Screen().setup(700, 500)
    t.Screen().colormode(255)
    t.tracer(25, 0)
    t.speed(0)
    t.up()

    def star(size, x, y):
        t.hideturtle()
        t.goto(x, y)
        t.setheading(randrange(360))  # Поворот звезды.
        for _ in range(5):
            t.forward(size)
            t.right(144)

    def play(counter):
        for _ in range(counter):
            color = (randrange(256), randrange(256), randrange(256))
            t.color(color)
            t.pencolor(color)
            t.begin_fill()

            x = randint(-330, 330)
            y = randint(-230, 230)
            size = randint(5, 30)  # Размер звезды.

            star(size, x, y)
            t.end_fill()

    counter = 80  # Кол-во звезд.
    play(counter)


def regular_polygon():
    """
    Рисует изображение правильных многоугольников по образцу.
    Многоугольники должны иметь разный цвет.
    n - кол-во сторон.
    a - длина сторон.
    """

    t.Screen().colormode(255)
    t.pensize(4)

    def polygon(n, size, x, y):
        angle = ((n - 2) * 180) / n

        a = (size * 4 * tan(radians(180 / n)) / n) ** 0.5

        t.hideturtle()
        t.up()
        t.goto(x, y)
        t.down()

        for i in range(n):
            t.forward(a)
            t.right(180 - angle)

    def play(counter):
        line = 50
        size = 1000
        for i in range(int(counter / 5)):
            for j in range(int(counter / 5)):
                n = randrange(3, 7)
                color = (randrange(256), randrange(256), randrange(256))
                t.color(color)
                t.pencolor('black')
                t.begin_fill()
                polygon(n, size, j + (j * line * 2), i + (i * line * 2))
                t.end_fill()

    play(25)


def chess():
    """Рисует изображение шахматной доски по образцу."""
    t.Screen().setup(520, 520)
    t.speed(0)
    turt = t.Turtle()
    turt.speed(0)
    turt.pensize(4)
    turt.up()
    turt.goto(-250, 250)
    turt.down()

    for _ in range(4):
        turt.forward(500)
        turt.right(90)

    color = ['black', 'white']

    def squre(color):
        t.color(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.right(90)
        t.end_fill()

    def play():
        for i in range(5):
            for j in range(5):
                t.up()
                if i % 2 == 0:
                    if j % 2 == 0:
                        t.goto(-250 + (j * 100), 250 - (i * 100))
                        squre(color[0])
                else:
                    if j % 2 == 1:
                        t.goto(-250 + (j * 100), 250 - (i * 100))
                        squre(color[0])

    play()


def compass():
    """Рисует изображение компаса по образцу."""

    t.up()
    t.goto(0, -100)
    t.down()
    t.pensize(4)
    t.circle(100)
    t.up()
    t.goto(0, 0)
    t.down()

    sides_light = ['Восток', 'Север', 'Запад', 'Юг']
    size = 250
    for sides in sides_light:
        t.forward(size)
        t.up()
        t.forward(40)
        t.write(sides, align='center', font=('Arial', 16, 'normal'))
        t.backward(size + 40)
        t.left(90)
        t.down()


def solar_system():
    """Рисует солнечную систему по образцу."""
    t.Screen().setup(1000, 500)
    t.Screen().bgcolor('black')

    def planet(name, size, color, x, y):
        sun = t.Turtle()
        sun.hideturtle()
        sun.speed(0)
        sun.up()
        sun.goto(x, y)
        sun.down()
        sun.color(color)
        sun.begin_fill()
        sun.circle(size)
        sun.end_fill()
        sun.up()
        sun.goto(x, y-20)
        sun.down()
        sun.write(name, align='center')

    planet('Солнце', 500, 'yellow', -800, -450)
    planet('Меркурий', 10, 'grey', -250, -10)
    planet('Венера', 15, 'orange', -200, -15)
    planet('Земля', 15, 'blue', -150, -15)
    planet('Марс', 10, 'red', -100, -10)
    planet('Юпитер', 100, 'grey', 50, -100)

    d = {
        'Солнце': {
            'size': 500,
            'x': -800,
            'y': -450},
        'Меркурий': {
            'size': 10,
            'x': -250,
            'y': -10},
    }

def main():
    t.showturtle()
    t.hideturtle()
    solar_system()
    # compass()
    # chess()
    # regular_polygon()
    # set_stars()
    # test()
    # animated_image_phases_moon()
    # draws_image_crescent_moon()
    # draws_rainbow_image()
    # optical_illusion()
    # traffic_lights()
    # draw_home()
    # snowflakes()
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
