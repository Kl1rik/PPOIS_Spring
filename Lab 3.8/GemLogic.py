import pygame
import sys
from pygame.locals import *
import random
import time
import datetime
import sqlite3
import math
import sys

from ScoreTable import formalize_rows as rows
from ScoreTable import find_max,insert

import Menu3


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

class Candy:
    
    def __init__(self, row_num, col_num):
        
        # set the candy's position on the board
        self.row_num = row_num
        self.col_num = col_num
        
        # assign a random image
        self.color = random.choice(candy_colors)
        image_name = f'swirl_{self.color}.png'
        self.image = pygame.image.load(image_name)
        self.image = pygame.transform.smoothscale(self.image, candy_size)
        self.rect = self.image.get_rect()
        self.rect.left = col_num * candy_width
        self.rect.top = row_num * candy_height
    def draw(self):
        screen.blit(self.image, self.rect)

    def snap(self):
        self.snap_row()
        self.snap_col()
        
    def snap_row(self):
        self.rect.top = self.row_num * candy_height
        
    def snap_col(self):
        self.rect.left = self.col_num * candy_width
board = []
for row_num in range(height // candy_height):
    
    # add a new row to the board
    board.append([])
    
    for col_num in range(width // candy_width):
        
        # create the candy and add it to the board
        candy = Candy(row_num, col_num)
        board[row_num].append(candy)
        


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 



def swap(candy1, candy2):
    
    temp_row = candy1.row_num
    temp_col = candy1.col_num
    
    candy1.row_num = candy2.row_num
    candy1.col_num = candy2.col_num
    
    candy2.row_num = temp_row
    candy2.col_num = temp_col
    
    # update the candies on the board list
    board[candy1.row_num][candy1.col_num] = candy1
    board[candy2.row_num][candy2.col_num] = candy2
    
    # snap them into their board positions
    candy1.snap()
    candy2.snap()
    

def find_matches(candy, matches):
    
    # add the candy to the set
    matches.add(candy)
    
    # check the candy above if it's the same color
    if candy.row_num > 0:
        neighbor = board[candy.row_num - 1][candy.col_num]
        if candy.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    # check the candy below if it's the same color
    if candy.row_num < height / candy_height - 1:
        neighbor = board[candy.row_num + 1][candy.col_num]
        if candy.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    # check the candy to the left if it's the same color
    if candy.col_num > 0:
        neighbor = board[candy.row_num][candy.col_num - 1]
        if candy.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    # check the candy to the right if it's the same color
    if candy.col_num < width / candy_width - 1:
        neighbor = board[candy.row_num][candy.col_num + 1]
        if candy.color == neighbor.color and neighbor not in matches:
            matches.update(find_matches(neighbor, matches))
            
    return matches
    

def match_three(candy):
    
    matches = find_matches(candy, set())
    if len(matches) >= 3:
        return matches
    else:
        return set()
    


    


Menu.main_menu()

