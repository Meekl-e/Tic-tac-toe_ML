from creations import canvas
import botClass
import random
import time


def checkWin(matrix):
    win_lines = [[0, 1, 2],  # первая строка
                 [3, 4, 5],  # вторая строка
                 [6, 7, 8],  # третья строка
                 [0, 3, 6],  # первый столбец
                 [1, 4, 7],  # второй столбец
                 [2, 5, 8],  # третий столбец
                 [0, 4, 8],  # диагональ
                 [2, 4, 6]]  # диагональ

    for line in win_lines:


        if len(set(map(lambda x: matrix[x],line))) == 1 and set(map(lambda x: matrix[x],line)) != {''}:
            return set(map(lambda x: matrix[x],line)).pop()

    return None

matrix = [""]*9
canvas = canvas("0")
bots = [botClass.bot("X"), botClass.bot("0")]

# программа обучения

c = 0
wins = {"X":0,"0":0}
while True:
    matrix = [""] * 9
    choice = random.sample([True,False], 1)[0]
    while checkWin(matrix) == None and any(map(lambda x: x == "", matrix)):
        if choice:
            choice = False
            canvas.update(bots[0].makeChoice(matrix))

        else:
            choice = True
            canvas.update(bots[1].makeChoice(matrix))
        matrix = canvas.getMatrix()


        #canvas.root.update()
        #time.sleep(0.5)


    winner = checkWin(matrix)
    if winner == None:
        for b in bots:
            b.export()
       # print("НИЧЬЯ")
    else:
        wins[winner]+=1
        for b in bots:
            if b.type == winner:
                b.win()
            else:
                b.lose()
    c+=1
    if c == 100:
        c = 0
        print(wins)

       # print("ВЫИГРАЛИ", winner)

'''

# программа игры

while checkWin(matrix) == None and any(map(lambda x:x=="",matrix)):
    while canvas.choice:
        canvas.root.update()
        time.sleep(0.1)
    matrix = canvas.getMatrix()
    if checkWin(matrix) != None or all(map(lambda x:x!="",matrix)):
        break
    canvas.update(bots[0].makeChoice(matrix))

    matrix = canvas.getMatrix()
    canvas.choice = True
    
winner = checkWin(matrix)
if winner == None:
    for b in bots:
        b.export()
    print("НИЧЬЯ")
else:
    for b in bots:
        if b.type == winner:
            b.win()


    print("ВЫИГРАЛИ",winner)
#'''
