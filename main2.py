import os, keyboard, time, colored

width = 50
height = 20
cells = [(col, row) for row in range(height) for col in range(width)]
x_speed = 0.5
y_speed = 0.5
score1 = 0
score2 = 0
ball = (width // 2, height // 2)

player1 = []
player2 = []

directions = {"right":(1, 0), "left":(-1, 0), "stop": (0, 0)}
direction = directions["stop"]
direction2 = directions["stop"]

for i in range(15):
    player1.append((width//2-i, height - 3))
    player2.append((width//2-i, 2))


def print_field():
    for cell in cells:
        if cell[0] in (0, width - 1) or cell[1] in (0, height - 1): 
            print("{0}#{1}".format(colored.fg("blue"), colored.attr(0)), end="")

        elif cell in player1:
            print("{0}-{1}".format(colored.fg("red"), colored.attr(0)), end="")

        elif cell in player2:
            print("{0}-{1}".format(colored.fg("red"), colored.attr(0)), end="")

        elif cell == ball:
            print("{0}*{1}".format(colored.fg("yellow"), colored.attr(0)), end="")

        else:
            print(" ", end="")


        if cell[0] == width - 1:
            print("")

    print(f"Player 1 score: {score1}")
    print(f"Player 2 score: {score2}")


def update():
    global ball, x_speed, y_speed, score1, score2
    ball = (ball[0]+x_speed,ball[1]+y_speed)

    if direction != directions["stop"]:
        for i, s in enumerate(player1):
            new = player1[i][0] + direction[0], player1[i][1]+direction[1]
            player1.remove(s)
            player1.insert(0, new)

    if direction2 != directions["stop"]:
        for i, s in enumerate(player2):
            new = player2[i][0] + direction2[0], player2[i][1]+direction2[1]
            player2.remove(s)
            player2.insert(0, new)

    for i in player1:
        for a in player2:
            if ball[1] == i[1] and ball[0] == i[0]:
                y_speed = y_speed * -1

            if ball[1] == a[1] and ball[0] == a[0]:
                y_speed = y_speed * -1

            if ball[0] == width - 1 or ball[0] == 0:
                x_speed = x_speed * -1

            if ball[1] == height - 1:
                score1 += 1
                ball = (width//2, height//2)
                x_speed = x_speed * -1
                y_speed = y_speed * -1

            if ball[1] == 1:
                score2 += 1
                ball = (width//2, height//2)
                x_speed = x_speed * -1
                y_speed = y_speed * -1


def left(i):
    global direction
    direction = directions["left"]

def right(i):
    global direction
    direction = directions["right"]

def left2(i):
    global direction2
    direction2 = directions["left"]

def right2(i):
    global direction2
    direction2 = directions["right"]

while True:
    os.system('cls')
    print_field()
    keyboard.on_press_key("left arrow", left)
    keyboard.on_press_key("right arrow", right)
    keyboard.on_press_key("a", left2)
    keyboard.on_press_key("d", right2)

    time.sleep(0.05)

    update()
    direction = directions["stop"]
    direction2 = directions["stop"]
