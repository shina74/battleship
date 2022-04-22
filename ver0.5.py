from Field import Field
from Ship import Ship
import random


field = [[], [], [], [], [], []]
com_field = [[], [], [], [], [], []]
count = [3, 2, 2, 1, 1, 1]
my_ships = []
com_ships = []
check = []
c_w = 10
m_w = 10

for i in range(6):
    for j in range(6):
        field[i].append(Field(i+1, j+1))

for i in range(6):
    for j in range(6):
        com_field[i].append(Field(i+1, j+1))


def shoot(a):
    xy = input("Капитан! Ждем координаты для выстрела!") if a == com_field else (
     random.randint(1, 6), random.randint(1, 6))
    try:
        x = int(xy[0]) - 1
        y = int(xy[-1]) - 1
    except ValueError:
        y = 10
    except IndexError:
        y = 10
    while len(xy) < 2 or\
            y > 5 or \
            x > 5 or \
            y < 0 or \
            x < 0 or \
            a[y][x].check:
        xy = input("Капитан! Координаты не верны!") if a == com_field else (random.randint(1, 6), random.randint(1, 6))
        try:
            x = int(xy[0]) - 1
            y = int(xy[-1]) - 1
        except ValueError:
            y = 10
        except IndexError:
            y = 10

    a[y][x].shoot = a[y][x].shoot


def win(a):
    count = 0
    for i in a:
        for j in i:
            if j.win:
                count += 1
    if count == 10: return True


def out(list):
    c = 1
    print('\t1\t2\t3\t4\t5\t6')
    for i in list:
        print(c, end="")
        c += 1
        for j in i:
            print(j.get, end="")
        print("")
    print('\n')


#далее идет большой кусок кода для расстоновки кораблей компьютера
for i in count:

    a = random.randint(0, 1)
    xy = (random.randint(1, 6), random.randint(1, 6))
    q = xy[0] if a else xy[-1]
    w = (int(xy[0]) + i - 1, int(xy[-1])) if a else (int(xy[0]), int(xy[-1]) + i - 1)
    while (int(xy[0]), int(xy[-1])) in check or \
            int(q) > (7 - i) or \
            w in check:
        a = random.randint(0, 1)
        xy = (random.randint(1, 6), random.randint(1, 6))
        q = xy[0] if a else xy[-1]
        w = (int(xy[0]) + i - 1, int(xy[-1])) if a else (int(xy[0]), int(xy[-1]) + i - 1)
    if a:
        for j in range(-1, i+1):
            check.append((int(xy[0]) + j, int(xy[-1]) - 1))
            check.append((int(xy[0]) + j, int(xy[-1])))
            check.append((int(xy[0]) + j, int(xy[-1]) + 1))
    else:
        for j in range(-1, i+1):
            check.append((int(xy[0]) - 1, int(xy[-1]) + j))
            check.append((int(xy[0]), int(xy[-1]) + j))
            check.append((int(xy[0]) + 1, int(xy[-1]) + j))

    com_ships.append(Ship(int(xy[0])-1, int(xy[-1])-1, i, a, True))

    for j in range(com_ships[-1].n_len):
        x, y = com_ships[-1].x_y
        if com_ships[-1].n_arrow:
            x += j
        else:
            y += j
        com_field[y][x].put = False
check = []
out(com_field)


#еще больше кусок кода для расстановки наших кораблей
for i in count:
    a = True if (i != 1 and (input("Строить корабль по горизонтали?\nY/N?  ") in ["Y", 'y'])) else False
    xy = input("Координаты начала коробля: ")
    q = xy[0] if a else xy[-1]
    try:
        w = (int(xy[0]) + i - 1, int(xy[-1])) if a else (int(xy[0]), int(xy[-1]) + i - 1)
    except ValueError:
        pass
    while xy[0].isdigit() is False or \
            xy[-1].isdigit() is False or \
            len(xy) < 2 or \
            (0 < int(xy[0]) < 7) is False or \
            (0 < int(xy[-1]) < 7) is False or \
            (int(xy[0]), int(xy[-1])) in check or \
            int(q) > (7 - i) or \
            w in check:
        print("Вы не можете размистить здесь корабль!")
        a = True if (i != 1 and (input("Строить корабль по горизонтали?\nY/N?  ") in ["Y", 'y'])) else False
        xy = input("Координаты начала коробля: ")
        q = xy[0] if a else xy[-1]
        try:
            w = (int(xy[0]) + i - 1, int(xy[-1])) if a else (int(xy[0]), int(xy[-1]) + i - 1)
        except ValueError:
            pass
    if a:
        for j in range(-1, i+1):
            check.append((int(xy[0]) + j, int(xy[-1]) - 1))
            check.append((int(xy[0]) + j, int(xy[-1])))
            check.append((int(xy[0]) + j, int(xy[-1]) + 1))
    else:
        for j in range(-1, i+1):
            check.append((int(xy[0]) - 1, int(xy[-1]) + j))
            check.append((int(xy[0]), int(xy[-1]) + j))
            check.append((int(xy[0]) + 1, int(xy[-1]) + j))

    my_ships.append(Ship(int(xy[0])-1, int(xy[-1])-1, i, a, True))

    for j in range(my_ships[-1].n_len):
        x, y = my_ships[-1].x_y
        if my_ships[-1].n_arrow:
            x += j
        else:
            y += j
        field[y][x].put = False
    out(field)



while True:
    shoot(com_field)
    out(com_field)
    if win(com_field):
        print("Ваша Победа!")
        break
    shoot(field)
    out(field)
    if win(field):
        print("Победа КОМПЬЮТЕРА!")
        break