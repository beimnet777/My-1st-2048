from random import * 				# to create random numbers(2 and 4) and also random postion
import turtle   					# for the graphics user interface
from sys import exit 				# when the game end requirment is fullfiled to terminate the program
import time 
two048 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


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