import random
from time import sleep

width = 150
height = 40


def dead_all(width, height):
    store = [[0 for _ in range(height)] for _ in range(width)]
    return store


def random_all(width, height):
    store = [[0 for _ in range(height)] for _ in range(width)]
    i = 0
    while i < width:
        j = 0
        while j < height:
            randomnumb = random.random()
            if randomnumb > 0.5:
                store[i][j] = 1
            else:
                store[i][j] = 0
            j += 1
        i += 1
    return store


def calcnext(store, width, heigth):
    storenew = [[0 for _ in range(height)] for _ in range(width)]
    y = 0
    while y < heigth:
        x = 0
        while x < width:
            surrounding = 0
            if x == 0 and y == 0:
                surrounding = store[x + 1][y] + store[x][y + 1] + store[x + 1][y + 1]
            elif x + 1 == width and y == 0:
                surrounding = store[x - 1][y] + store[x - 1][y + 1] + store[x][y + 1]
            elif x == 0 and y + 1 == height:
                surrounding = store[x][y - 1] + store[x + 1][y - 1] + store[x + 1][y]
            elif x + 1 == width and y + 1 == height:
                surrounding = store[x - 1][y - 1] + store[x][y - 1] + store[x - 1][y]
            elif x == 0:
                surrounding = store[x][y - 1] + store[x + 1][y - 1] + store[x + 1][y] + store[x][y + 1] + store[x + 1][
                    y + 1]
            elif x + 1 == width:
                surrounding = store[x - 1][y - 1] + store[x][y - 1] + store[x - 1][y] + store[x - 1][y + 1] + store[x][
                    y + 1]
            elif y == 0:
                surrounding = store[x - 1][y] + store[x + 1][y] + store[x - 1][y + 1] + store[x][y + 1] + store[x + 1][
                    y + 1]
            elif y + 1 == height:
                surrounding = store[x - 1][y - 1] + store[x][y - 1] + store[x + 1][y - 1] + store[x - 1][y] + \
                              store[x + 1][y]
            else:
                surrounding = store[x - 1][y - 1] + store[x][y - 1] + store[x + 1][y - 1] + \
                              store[x - 1][y] + store[x + 1][y] + \
                              store[x - 1][y + 1] + store[x][y + 1] + store[x + 1][y + 1]
            if surrounding <= 1:
                storenew[x][y] = 0
            elif surrounding == 2:
                storenew[x][y] = 1 * store[x][y]
            elif surrounding == 3:
                storenew[x][y] = 1
            elif surrounding > 3:
                storenew[x][y] = 0
            x += 1
        y += 1
    store = storenew
    return store


def render(store, width, heigth):
    print("-" * width)
    y = 0
    while y < heigth:
        x = 0
        while x < width:
            if store[x][y] == 0:
                print(" ", end="")
            else:
                print(u"\u2588", end="")
            x += 1
        print("")
        y += 1
    print("-" * width)


store = random_all(width, height)
while True:
    store = calcnext(store, width, height)
    render(store, width, height)
    sleep(0.2)