import keyboard
import os, time, sys
from random import randint
import colored

score1 = 0
score2 = 0
def print_field():
    for cell in cells:
        if cell in player1:
            print("{0}-{1}".format(colored.fg("red"), colored.attr(0)), end = "")

        elif cell in player2:
            print("{0}-{1}".format(colored.fg("red"), colored.attr(0)), end = "")

        elif cell == ball:
            print("{0}*{1}".format(colored.fg("yellow"), colored.attr(0)), end = "")

        elif cell[0] in (0, width - 1) or cell[1] in (0, height - 1):
            print("{0}*{1}".format(colored.fg("blue"), colored.attr(0)), end = "")

        else:
            print(" ", end = "")

        if cell[0] == width - 1:
            print("")


    print(f"Player 1 score: {score1}")
    print(f"Player 2 score: {score2}")


def update():
    global ball, x_move, y_move, score2, score1
    if direction != directions["stop"]:
        for i, s in enumerate(player1):
            new_head = player1[i][0] + direction[0], player1[i][1] + direction[1]
            player1.remove(s)
            player1.insert(0, new_head)

    if direction2 != directions["stop"]:
        for i, s in enumerate(player2):
            new_head = player2[i][0] + direction2[0], player2[i][1] + direction2[1]
            player2.remove(s)
            player2.insert(0, new_head)
    
    
    for i in player1:
        for a in player2:
            if ball[1] == i[1] and ball[0] == i[0]:
                y_move = y_move * -1

            if ball[1] == a[1] and ball[0] == a[0]:
                y_move = y_move * -1

            elif ball[0] == 1:
                x_move = x_move * -1

            elif ball[0] == width - 1:
                x_move = x_move * -1

            elif ball[1] == height - 1 :
                score1 += 1
                ball = (width // 2, height // 2)
                x_move = x_move * -1
                y_move = y_move * -1

            elif ball[1] == 1 :
                score2 += 1
                ball = (width // 2, height // 2)
                x_move = x_move * -1
                y_move = y_move * -1



    ball = (ball[0] + +x_move, ball[1] + +y_move)

def left(s):
    global direction
    direction = directions["left"]

def right(s):
    global direction
    direction = directions["right"]

def left2(s):
    global direction2
    direction2 = directions["left"]

def right2(s):
    global direction2
    direction2 = directions["right"]

width = 50
height = 20
cells = [(col, row) for row in range(height) for col in range(width)]
player1 = []
player2 = []
for i in range(15):
    player1.append((width // 2 - i, height - 3))
    player2.append((width // 2 - i, 2))

    
ball = (width // 2 , height //2)
score = 0
directions = {"left": (-1, 0), "right":(1, 0), "stop":(0, 0)}
direction = directions["stop"]
direction2 = directions["stop"]
x_move = 0.5
y_move = 0.5


while True:
    os.system("cls")
    print_field()
    keyboard.on_press_key("left arrow", left)
    keyboard.on_press_key("right arrow", right)
    keyboard.on_press_key("a", left2)
    keyboard.on_press_key("d", right2)

    time.sleep(0.05)


    update()

    direction = directions["stop"]
    direction2 = directions["stop"]
