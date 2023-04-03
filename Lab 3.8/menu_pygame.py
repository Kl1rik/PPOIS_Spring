import pygame
import sys
from pygame.locals import *
import random
import time
import datetime
import sqlite3
import math

pygame.init()
pygame.display.set_caption('Jewel quest')
screen = pygame.display.set_mode((400, 425),0,32)

width = 400
height = 400
scoreboard_height = 25




# the adjacent candy that will be swapped with the clicked candy


    # coordinates of the point where the user clicked on

# game variables


start_ticks=pygame.time.get_ticks() #starter tick

# game loop

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
candy_colors = ['blue', 'green', 'orange', 'pink', 'purple', 'red', 'teal', 'yellow'] 
candy_width = 40
candy_height = 40
candy_size = (candy_width, candy_height)
"""
A function that can be used to write text on our screen and buttons
"""
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
 
# A variable to check for the status later


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
    
# find neighboring candies that match the candy's color
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
    
# return a set of at least 3 matching candies or an empty set
def match_three(candy):
    
    matches = find_matches(candy, set())
    if len(matches) >= 3:
        return matches
    else:
        return set()
    


    
# Main container function that holds the buttons and game functions
def main_menu():
    while True:
 
        screen.fill((173, 216, 230))
        draw_text('Game mode', font, (0,0,0), screen, 150, 40)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(150, 100, 100, 50)
        button_2 = pygame.Rect(150, 180, 100, 50)
        button_3 = pygame.Rect(150, 260, 100, 50)
        button_4 = pygame.Rect(150, 340, 100, 50)
        button_5 = pygame.Rect(10, 100, 100, 50)
        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                level_1()
        if button_3.collidepoint((mx, my)):
            if click:
                level_2()
        if button_4.collidepoint((mx, my)):
            if click:
                level_3()

        pygame.draw.rect(screen, (139, 0, 139), button_1)
        pygame.draw.rect(screen, (106, 90, 205), button_2)
        pygame.draw.rect(screen, (75, 0, 130), button_3)
        pygame.draw.rect(screen, (72, 61, 139), button_4)
        pygame.draw.rect(screen, (148,0,211), button_5)
        #writing text on top of button
        draw_text('Time ', font, (255,255,255), screen, 170, 115)
        draw_text(' Score 1', font, (255,255,255), screen, 155, 195)
        draw_text(' Score 2', font, (255,255,255), screen, 155, 275)
        draw_text(' Score 3', font, (255,255,255), screen, 155, 355)
        draw_text(' Highscore', font, (255,255,255), screen, 5, 115)



        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        
 
"""
This function is called when the "PLAY" button is clicked.
"""
 
    
def game():
    
    screen.fill((139, 0, 139))
    score = 0
    moves = 0
    time_limit = 10
    swapped_candy = None
    clicked_candy = None
    click_x = None
    click_y = None
    running = True
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for candy in row:
                candy.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 4, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 4, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves}', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 4, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)   
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  #calculate how many seconds
        if seconds>time_limit: # if more than 10 seconds close the game
            running = False
    
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # detect mouse click
            if clicked_candy is None and event.type == MOUSEBUTTONDOWN:
                
                # get the candy that was clicked on
                for row in board:
                    for candy in row:
                        if candy.rect.collidepoint(event.pos):
                            
                            clicked_candy = candy
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_candy is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped candy if direction of mouse motion changed
                if swapped_candy is not None:
                    swapped_candy.snap()
                    
                # determine the direction of the neighboring candy to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked candy to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_candy.snap_row()
                else:
                    clicked_candy.snap_col()
                    
                # if moving the clicked candy to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_candy.col_num > 0:
                    
                    # get the candy to the left
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num - 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width - distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left <= swapped_candy.col_num * candy_width + candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_candy.col_num < width / candy_width - 1:
                    
                    # get the candy to the right
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num + 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width + distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left >= swapped_candy.col_num * candy_width - candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_candy.row_num > 0:
                    
                    # get the candy above
                    swapped_candy = board[clicked_candy.row_num - 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height - distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top <= swapped_candy.row_num * candy_height + candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_candy.row_num < height / candy_height - 1:
                    
                    # get the candy below
                    swapped_candy = board[clicked_candy.row_num + 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height + distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top >= swapped_candy.row_num * candy_height - candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
            # detect mouse release
            if clicked_candy is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_candy.snap()
                clicked_candy = None
                if swapped_candy is not None:
                    swapped_candy.snap()
                    swapped_candy = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for candy in matches:
                    new_width = candy.image.get_width() - 1
                    new_height = candy.image.get_height() - 1
                    new_size = (new_width, new_height)
                    candy.image = pygame.transform.smoothscale(candy.image, new_size)
                    candy.rect.left = candy.col_num * candy_width + (candy_width - new_width) / 2
                    candy.rect.top = candy.row_num * candy_height + (candy_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        candy = board[row_num][col_num]
                        if candy.image.get_width() <= 0 or candy.image.get_height() <= 0:
                            matches.remove(candy)
                            
                            # generate a new candy
                            board[row_num][col_num] = Candy(row_num, col_num)
                            
                draw()
       
                pygame.display.update()
        

"""
This function is called when the "OPTIONS" button is clicked.
"""
def level_1():
    screen.fill((106, 90, 205))
    score = 0
    moves = 0
    score_limit = 10
    swapped_candy = None
    clicked_candy = None
    click_x = None
    click_y = None
    running = True
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for candy in row:
                candy.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score} / {score_limit}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 5, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 5, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves} ', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 5, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)

        level_text = font.render(f'Level 1 ', 1, (0, 0, 0))
        level_text_rect = level_text.get_rect(center=(width * 4 / 5, height + scoreboard_height / 2))
        screen.blit(level_text, level_text_rect)

        
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  #calculate how many seconds
        if score > score_limit:
            running = False
    
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # detect mouse click
            if clicked_candy is None and event.type == MOUSEBUTTONDOWN:
                
                # get the candy that was clicked on
                for row in board:
                    for candy in row:
                        if candy.rect.collidepoint(event.pos):
                            
                            clicked_candy = candy
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_candy is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped candy if direction of mouse motion changed
                if swapped_candy is not None:
                    swapped_candy.snap()
                    
                # determine the direction of the neighboring candy to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked candy to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_candy.snap_row()
                else:
                    clicked_candy.snap_col()
                    
                # if moving the clicked candy to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_candy.col_num > 0:
                    
                    # get the candy to the left
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num - 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width - distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left <= swapped_candy.col_num * candy_width + candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_candy.col_num < width / candy_width - 1:
                    
                    # get the candy to the right
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num + 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width + distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left >= swapped_candy.col_num * candy_width - candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_candy.row_num > 0:
                    
                    # get the candy above
                    swapped_candy = board[clicked_candy.row_num - 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height - distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top <= swapped_candy.row_num * candy_height + candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_candy.row_num < height / candy_height - 1:
                    
                    # get the candy below
                    swapped_candy = board[clicked_candy.row_num + 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height + distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top >= swapped_candy.row_num * candy_height - candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
            # detect mouse release
            if clicked_candy is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_candy.snap()
                clicked_candy = None
                if swapped_candy is not None:
                    swapped_candy.snap()
                    swapped_candy = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for candy in matches:
                    new_width = candy.image.get_width() - 1
                    new_height = candy.image.get_height() - 1
                    new_size = (new_width, new_height)
                    candy.image = pygame.transform.smoothscale(candy.image, new_size)
                    candy.rect.left = candy.col_num * candy_width + (candy_width - new_width) / 2
                    candy.rect.top = candy.row_num * candy_height + (candy_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        candy = board[row_num][col_num]
                        if candy.image.get_width() <= 0 or candy.image.get_height() <= 0:
                            matches.remove(candy)
                            
                            # generate a new candy
                            board[row_num][col_num] = Candy(row_num, col_num)
                            
                draw()
       
                pygame.display.update()
def level_2():
    screen.fill((106, 90, 205))
    score = 0
    moves = 0
    score_limit = 50
    swapped_candy = None
    clicked_candy = None
    click_x = None
    click_y = None
    running = True
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for candy in row:
                candy.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score} / {score_limit}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 5, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 5, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves} ', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 5, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)

        level_text = font.render(f'Level 2 ', 1, (0, 0, 0))
        level_text_rect = level_text.get_rect(center=(width * 4 / 5, height + scoreboard_height / 2))
        screen.blit(level_text, level_text_rect)

        
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  #calculate how many seconds
        if score > score_limit:
            running = False
    
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # detect mouse click
            if clicked_candy is None and event.type == MOUSEBUTTONDOWN:
                
                # get the candy that was clicked on
                for row in board:
                    for candy in row:
                        if candy.rect.collidepoint(event.pos):
                            
                            clicked_candy = candy
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_candy is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped candy if direction of mouse motion changed
                if swapped_candy is not None:
                    swapped_candy.snap()
                    
                # determine the direction of the neighboring candy to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked candy to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_candy.snap_row()
                else:
                    clicked_candy.snap_col()
                    
                # if moving the clicked candy to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_candy.col_num > 0:
                    
                    # get the candy to the left
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num - 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width - distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left <= swapped_candy.col_num * candy_width + candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_candy.col_num < width / candy_width - 1:
                    
                    # get the candy to the right
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num + 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width + distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left >= swapped_candy.col_num * candy_width - candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_candy.row_num > 0:
                    
                    # get the candy above
                    swapped_candy = board[clicked_candy.row_num - 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height - distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top <= swapped_candy.row_num * candy_height + candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_candy.row_num < height / candy_height - 1:
                    
                    # get the candy below
                    swapped_candy = board[clicked_candy.row_num + 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height + distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top >= swapped_candy.row_num * candy_height - candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
            # detect mouse release
            if clicked_candy is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_candy.snap()
                clicked_candy = None
                if swapped_candy is not None:
                    swapped_candy.snap()
                    swapped_candy = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for candy in matches:
                    new_width = candy.image.get_width() - 1
                    new_height = candy.image.get_height() - 1
                    new_size = (new_width, new_height)
                    candy.image = pygame.transform.smoothscale(candy.image, new_size)
                    candy.rect.left = candy.col_num * candy_width + (candy_width - new_width) / 2
                    candy.rect.top = candy.row_num * candy_height + (candy_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        candy = board[row_num][col_num]
                        if candy.image.get_width() <= 0 or candy.image.get_height() <= 0:
                            matches.remove(candy)
                            
                            # generate a new candy
                            board[row_num][col_num] = Candy(row_num, col_num)
                            
                draw()
       
                pygame.display.update()        

def level_3():
    screen.fill((106, 90, 205))
    score = 0
    moves = 0
    score_limit = 500
    swapped_candy = None
    clicked_candy = None
    click_x = None
    click_y = None
    running = True
    width = 200
    height = 200
    def draw():
    
    # draw the background
        pygame.draw.rect(screen, (173, 216, 230), (0, 0, width, height + scoreboard_height))
        
        # draw the candies
        for row in board:
            for candy in row:
                candy.draw()
        
        # display the score and moves
        font = pygame.font.SysFont('monoface', 18)
        score_text = font.render(f'Score: {score} / {score_limit}', 1, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(width / 5, height + scoreboard_height / 2))
        screen.blit(score_text, score_text_rect)
        
        timer_text = font.render(f'Timer: {seconds_format}', 1, (0, 0, 0))
        timer_text_rect = timer_text.get_rect(center=(width * 2 / 5, height + scoreboard_height / 2))
        screen.blit(timer_text, timer_text_rect)

        moves_text = font.render(f'Moves: {moves} ', 1, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(width * 3 / 5, height + scoreboard_height / 2))
        screen.blit(moves_text, moves_text_rect)

        level_text = font.render(f'Level 3 ', 1, (0, 0, 0))
        level_text_rect = level_text.get_rect(center=(width * 4 / 5, height + scoreboard_height / 2))
        screen.blit(level_text, level_text_rect)

        
    while running:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        seconds_format = math.trunc(seconds)  #calculate how many seconds
        if score > score_limit:
            running = False
    
        # set of matching candies
        matches = set()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
            # detect mouse click
            if clicked_candy is None and event.type == MOUSEBUTTONDOWN:
                
                # get the candy that was clicked on
                for row in board:
                    for candy in row:
                        if candy.rect.collidepoint(event.pos):
                            
                            clicked_candy = candy
                            
                            # save the coordinates of the point where the user clicked
                            click_x = event.pos[0]
                            click_y = event.pos[1]
                            
            # detect mouse motion
            if clicked_candy is not None and event.type == MOUSEMOTION:
                
                # calculate the distance between the point the user clicked on
                # and the current location of the mouse cursor
                distance_x = abs(click_x - event.pos[0])
                distance_y = abs(click_y - event.pos[1])
                
                # reset the position of the swapped candy if direction of mouse motion changed
                if swapped_candy is not None:
                    swapped_candy.snap()
                    
                # determine the direction of the neighboring candy to swap with
                if distance_x > distance_y and click_x > event.pos[0]:
                    direction = 'left'
                elif distance_x > distance_y and click_x < event.pos[0]:
                    direction = 'right'
                elif distance_y > distance_x and click_y > event.pos[1]:
                    direction = 'up'
                else:
                    direction = 'down'
                    
                # if moving left/right, snap the clicked candy to its row position
                # otherwise, snap it to its col position
                if direction in ['left', 'right']:
                    clicked_candy.snap_row()
                else:
                    clicked_candy.snap_col()
                    
                # if moving the clicked candy to the left,
                # make sureit's not on the first col
                if direction == 'left' and clicked_candy.col_num > 0:
                    
                    # get the candy to the left
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num - 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width - distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width + distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left <= swapped_candy.col_num * candy_width + candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy to the right,
                # make sure it's not on the last col
                if direction == 'right' and clicked_candy.col_num < width / candy_width - 1:
                    
                    # get the candy to the right
                    swapped_candy = board[clicked_candy.row_num][clicked_candy.col_num + 1]
                    
                    # move the two candies
                    clicked_candy.rect.left = clicked_candy.col_num * candy_width + distance_x
                    swapped_candy.rect.left = swapped_candy.col_num * candy_width - distance_x
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.left >= swapped_candy.col_num * candy_width - candy_width / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy up,
                # make sure it's not on the first row
                if direction == 'up' and clicked_candy.row_num > 0:
                    
                    # get the candy above
                    swapped_candy = board[clicked_candy.row_num - 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height - distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height + distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top <= swapped_candy.row_num * candy_height + candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
                # if moving the clicked candy down,
                # make sure it's not on the last row
                if direction == 'down' and clicked_candy.row_num < height / candy_height - 1:
                    
                    # get the candy below
                    swapped_candy = board[clicked_candy.row_num + 1][clicked_candy.col_num]
                    
                    # move the two candies
                    clicked_candy.rect.top = clicked_candy.row_num * candy_height + distance_y
                    swapped_candy.rect.top = swapped_candy.row_num * candy_height - distance_y
                    
                    # snap them into their new positions on the board
                    if clicked_candy.rect.top >= swapped_candy.row_num * candy_height - candy_height / 4:
                        swap(clicked_candy, swapped_candy)
                        matches.update(match_three(clicked_candy))
                        matches.update(match_three(swapped_candy))
                        moves += 1
                        clicked_candy = None
                        swapped_candy = None
                        
            # detect mouse release
            if clicked_candy is not None and event.type == MOUSEBUTTONUP:
                
                # snap the candies back to their original positions on the grid
                clicked_candy.snap()
                clicked_candy = None
                if swapped_candy is not None:
                    swapped_candy.snap()
                    swapped_candy = None
                
        draw()
        pygame.display.update()
        
        # check if there's at least 3 matching candies
        if len(matches) >= 3:
            
            # add to score
            score += len(matches)
            
            # animate the matching candies shrinking
            while len(matches) > 0:
                
                clock.tick(100)
                
                # decrease width and height by 1
                for candy in matches:
                    new_width = candy.image.get_width() - 1
                    new_height = candy.image.get_height() - 1
                    new_size = (new_width, new_height)
                    candy.image = pygame.transform.smoothscale(candy.image, new_size)
                    candy.rect.left = candy.col_num * candy_width + (candy_width - new_width) / 2
                    candy.rect.top = candy.row_num * candy_height + (candy_height - new_height) / 2
                    
                # check if the candies have shrunk to zero size
                for row_num in range(len(board)):
                    for col_num in range(len(board[row_num])):
                        candy = board[row_num][col_num]
                        if candy.image.get_width() <= 0 or candy.image.get_height() <= 0:
                            matches.remove(candy)
                            
                            # generate a new candy
                            board[row_num][col_num] = Candy(row_num, col_num)
                            
                draw()
       
                pygame.display.update()       

main_menu()