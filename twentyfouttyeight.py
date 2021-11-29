from random import * 				# to create random numbers(2 and 4) and also random postion
import turtle   					# for the graphics user interface
from sys import exit 				# when the game end requirment is fullfiled to terminate the program
import time 
two048 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
writer = turtle.Turtle()
writer.color('#5d0d9e')
writer_2=turtle.Turtle()
writer_2.ht()
writer_2.penup()
writer_2.setpos(-220,-300)
writer_2.pendown()
writer_2.write("USE THE ARROWS TO PLAY",font=('verdana',25))
writer_2.penup()
writer_2.setpos(-100,-90)
writer_2.pendown()


def setters():
    pos1_row= randint(0, 3)
    pos1_column = randint(0, 3)
    two048[pos1_row][pos1_column] = randrange(2, 5, 2)
    for i in range(3):
        pos2_row = randint(0, 3)
        pos2_column= randint(0, 3)
        if (pos1_row, pos1_column) != (pos2_row, pos2_column) and (pos1_row, pos1_column) != (pos2_column, pos2_row):
            two048[pos2_row][pos2_column] = randrange(2, 5, 2)
            break
        else:
            continue
# to generate random number(2 or 4) and assign it to random position
def merge_right():
    counter=5
    direction = 1
    amount = 3
    for k in range(3):
        for i in range(4):
            for j in range(4):
                if j != amount:
                    if two048[i][j + direction] == 0:
                        two048[i][j + direction] = two048[i][j]
                        two048[i][j] = 0
                    elif counter != i and (two048[i][j + direction] == two048[i][j]):
                        two048[i][j + direction] = 2 * two048[i][j]
                        two048[i][j] = 0
                        counter = i
    setters_2()
    writer.clear()
    apperance_updater()
    if game_checker() !=0:
        writer_2.write("GAME OVER YOUR SCORE IS :",font=('verdana',20))
        writer_2.penup()
        writer_2.setpos(320,-90)
        writer_2.pendown()
        writer_2.write(game_checker(),font=('verdana',20))
        time.sleep(5)
        exit()
# merging to the right and checking possiblities to continue the game 
    
def merge_left():
    counter=5
    direction = -1
    amount = 0
    for k in range(3):
        for i in range(4):
            for j in range(4):
                if j != amount:
                    if two048[i][j + direction] == 0:
                        two048[i][j + direction] = two048[i][j]
                        two048[i][j] = 0
                    elif counter != i and (two048[i][j + direction] == two048[i][j]):
                        two048[i][j + direction] = 2 * two048[i][j]
                        two048[i][j] = 0
                        counter = i
    setters_2()
    writer.clear()
    apperance_updater()
    if game_checker() !=0:
        writer_2.write("GAME OVER YOUR SCORE IS :",font=('verdana',20))
        writer_2.penup()
        writer_2.setpos(320,-90)
        writer_2.pendown()
        writer_2.write(game_checker(),font=('verdana',20))
        time.sleep(5)
        exit()

# merging to the left and checking possiblities to continue the game
    
def merge_down():
    counter=5
    direction_2 = 1
    amount = 3
    for k in range(3):
        for i in range(4):
            for j in range(4):
                if i != amount:
                    if two048[i + direction_2][j] == 0:
                        two048[i + direction_2][j] = two048[i][j]
                        two048[i][j] = 0
                    elif counter != j and two048[i + direction_2][j] == two048[i][j]:
                        two048[i + direction_2][j] = 2 * two048[i][j]
                        two048[i][j] = 0
                        counter = j
    setters_2()
    writer.clear()
    apperance_updater()
    if game_checker() !=0:
        writer_2.write("GAME OVER YOUR SCORE IS :",font=('verdana',20))
        writer_2.penup()
        writer_2.setpos(320,-90)
        writer_2.pendown()
        writer_2.write(game_checker(),font=('verdana',20))
        time.sleep(5)
        exit()
 
# merging down and checking possiblities to continue the game   
def merge_up():
    counter=5
    direction_2 = -1
    amount = 0
    for k in range(3):
        for i in range(4):
            for j in range(4):
                if i != amount:
                    if two048[i + direction_2][j] == 0:
                        two048[i + direction_2][j] = two048[i][j]
                        two048[i][j] = 0
                    elif counter != j and two048[i + direction_2][j] == two048[i][j]:
                        two048[i + direction_2][j] = 2 * two048[i][j]
                        two048[i][j] = 0
                        counter = j
    setters_2()
    writer.clear()
    apperance_updater()
    if game_checker() !=0:
        writer_2.write("GAME OVER YOUR SCORE IS :",font=('verdana',20))
        writer_2.penup()
        writer_2.setpos(320,-90)
        writer_2.pendown()
        writer_2.write(game_checker(),font=('verdana',20))
        time.sleep(5)
        exit()

# merging up and checking possiblities to continue the game
    
def setters_2():
    for i in range (30):
        pos1_row = randint(0, 3)
        pos1_column = randint(0, 3)
        if two048[pos1_row][pos1_column] == 0:
            two048[pos1_row][pos1_column]=randrange(2,5,2) 
            break
        else:
            continue  
# gernetaingn random number at the random postion after the game started 

def game_checker():
    max=0
    for i in range(4):
        for j in range(4):
            if two048[i][j] == 0:
                return 0
            else:
                if two048[i][j]>max:
                    max=two048[i][j]
    return max

 #checking weather all of the squares are full or not and returning numbe rfor further descision
def apperance_updater():
    turtle.tracer(1,0)
    writer.ht()
    writer.pensize(10)
    xpos = -220
    for i in range(4):
        ypos = 30
        for j in range(4):
            writer.penup()
            writer.setpos(xpos, ypos)
            writer.pendown()
            if two048[i][j] != 0:
                writer.write(two048[i][j], font=("verdana", 25))
            ypos += 80
        xpos += 120

#to update what is diplayed on the gui evry time a specified key is pressed
box= turtle.Turtle()
box.pensize(6)
box.color('#000000')
screen = turtle.Screen()
screen.bgcolor('#adadad')
screen.title('2048 BY BEIMNET BEKELE')
box.ht()
pos_change = 80
box.penup()
box.backward(240)
box.pendown()
turtle.tracer(3, 0)
for i in range(4):
    for j in range(2):
        box.forward(480)
        box.left(90)
        box.forward(80)
        box.left(90)
    box.setpos(-240, pos_change)
    pos_change += 80
box_divider = turtle.Turtle()
box_divider.pensize(6)
box_divider.color('#000000')
box_divider.ht()
box_divider.penup()
box_divider.backward(240)
box_divider.pendown()
for i in range(2):
    box_divider.forward(120)
    box_divider.left(90)
    box_divider.forward(320)
    box_divider.right(90)
    box_divider.forward(120)
    box_divider.right(90)
    box_divider.forward(320)
    box_divider.left(90)

# creating the squre     