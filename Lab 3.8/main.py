import pygame
import sys
from pygame.locals import *
import random
import time
import datetime
import sqlite3
import math
import sys
from GemLogic import draw_text
from GemLogic import Candy
from GemLogic import swap
from GemLogic import match_three
from ScoreTable import find_max,insert
from ScoreTable import formalize_rows as rows
from Menu3 import Menu
pygame.init()
pygame.display.set_caption('Jewel quest')
screen = pygame.display.set_mode((400, 425),0,32)

width = 400
height = 400
scoreboard_height = 25


start_ticks=pygame.time.get_ticks() 

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
candy_colors = ['blue', 'green', 'orange', 'pink', 'purple', 'red', 'teal', 'yellow'] 
candy_width = 40
candy_height = 40
candy_size = (candy_width, candy_height)
board = []
for row_num in range(height // candy_height):
    
    # add a new row to the board
    board.append([])
    
    for col_num in range(width // candy_width):
        
        # create the candy and add it to the board
        candy = Candy(row_num, col_num)
        board[row_num].append(candy)
Menu.main_menu()