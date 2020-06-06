from ufo_moving import *
import turtle as tr
tr.tracer(0)
tr.hideturtle()

ufo1 = (Ufo('Пришелец-1', 100, 100, 7, 150, 'green', 5, 6))
ufo1.show()
tr.update()
ufo2 = (Ufo('Пришелец-2', -100, -100, 5, 200, 'red', 3, 4))
ufo2.show()
while True:
    ufo1.Nastya()
    ufo1.random()
    ufo1.show()
    ufo2.Nastya()
    ufo2.random()
    ufo2.show()
    tr.update()