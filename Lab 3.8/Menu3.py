import pygame
import sys
from pygame.locals import *
import random
import time
import datetime
import sqlite3
import math
import sys
sys.path.append("C:\\Users\\kyrill\\Documents\\GitHub\\PPOIS_Spring\\Lab 3.8")
from GemLogic import draw_text
from GemLogic import Candy
from GemLogic import swap
from GemLogic import match_three
from ScoreTable import formalize_rows as rows
from ScoreTable import find_max
from ScoreTable import insert


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
        
class Menu():
    def main_menu(self):
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
            button_6 = pygame.Rect(10, 180, 100, 50)
            button_7 = pygame.Rect(10, 260, 100, 50)
            #defining functions when a certain button is pressed
            if button_1.collidepoint((mx, my)):
                if click:
                    self.game()
            if button_2.collidepoint((mx, my)):
                if click:
                    self.level_1()
            if button_3.collidepoint((mx, my)):
                if click:
                    self.level_2()
            if button_4.collidepoint((mx, my)):
                if click:
                    self.level_3()
            if button_5.collidepoint((mx, my)):
                if click:
                    self.score()
            if button_6.collidepoint((mx, my)):
                if click:
                    self.help()
            if button_7.collidepoint((mx, my)):
                if click:
                    pygame.quit()        
            pygame.draw.rect(screen, (139, 0, 139), button_1)
            pygame.draw.rect(screen, (106, 90, 205), button_2)
            pygame.draw.rect(screen, (75, 0, 130), button_3)
            pygame.draw.rect(screen, (72, 61, 139), button_4)
            pygame.draw.rect(screen, (148,0,211), button_5)
            pygame.draw.rect(screen, (153,0,76), button_6)
            pygame.draw.rect(screen, (235,60,95), button_7)
            #writing text on top of button
            draw_text('Time ', font, (255,255,255), screen, 170, 115)
            draw_text(' Score 1', font, (255,255,255), screen, 155, 195)
            draw_text(' Score 2', font, (255,255,255), screen, 155, 275)
            draw_text(' Score 3', font, (255,255,255), screen, 155, 355)
            draw_text(' Highscore', font, (255,255,255), screen, 5, 115)
            draw_text('     Help', font, (255,255,255), screen, 5, 195)
            draw_text('    Close', font, (255,255,255), screen, 5, 275)



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
    This function is called when the "Time" button is clicked.
    """
    
        
    def game(self):
        
        screen.fill((139, 0, 139))
        score = 0
        moves = 0
        time_limit = 60
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
            seconds_format = math.trunc(seconds)  
            if seconds>time_limit:
                running = False
                if score > find_max(): 
                    
                    self.win_screen(score)
                # 
                #         insert('Kain',score)
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
    This functions is called when the "level *" button is clicked.
    """
    def level_1(self):
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
                self.complete_level_screen()
        
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
    def level_2(self):
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
                self.complete_level_screen()
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

    def level_3(self):
        screen.fill((106, 90, 205))
        score = 0
        moves = 0
        score_limit = 500
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

            level_text = font.render(f'Level 3 ', 1, (0, 0, 0))
            level_text_rect = level_text.get_rect(center=(width * 4 / 5, height + scoreboard_height / 2))
            screen.blit(level_text, level_text_rect)

            
        while running:
            seconds=(pygame.time.get_ticks()-start_ticks)/1000
            seconds_format = math.trunc(seconds)  #calculate how many seconds
            if score > score_limit:
                running = False
                self.complete_level_screen()
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

    def score(self):
        running = True
        while running:
            screen.fill((207, 140, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            draw_text('Score Table', font, (0,0,0), screen, 150, 40)
            for i in range(len(rows)):
                draw_text(rows[i], font, (255,255,255), screen, 155, 105 + 60 * i)
            
            pygame.display.update()
    def win_screen(self,score_level):
        
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(100, 200, 200, 32)
        text = ''
        text_surface = font.render(text, True, (255, 255, 255))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        print("User input:", text)
                        insert(text,score_level)
                        text = ''
                        
                    else:
                        text += event.unicode
                    text_surface = font.render(text, True, (255, 255, 255))

            screen.fill((0, 128, 0))
            pygame.draw.rect(screen, (32, 178, 170), input_box, 2)
            screen.blit(text_surface, (input_box.x+5, input_box.y+5))
            draw_text('  Congratulations', font, (0,0,0), screen, 100, 40)
            draw_text(' This is new record', font, (0,0,0), screen, 100, 80)
            draw_text(' Enter your Name ', font, (0,0,0), screen, 90, 120)
            pygame.display.flip()

    def complete_level_screen(self):
        font = pygame.font.Font(None, 32)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    

            screen.fill((0, 255, 153))
            
            draw_text('Level complete', font, (0,0,0), screen, 90, 200)
            
            pygame.display.flip()

    def help(self):
        running = True
        while running:
            screen.fill((255, 242, 145))
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            draw_text('Rules', font, (0,0,0), screen, 80, 40)
            draw_text('Classic match-tree rules', font, (0,0,0), screen, 80, 80)
            draw_text('Time: Play until time end', font, (0,0,0), screen, 80, 120)
            draw_text('Score *: 3 level with limit score', font, (0,0,0), screen, 80, 160)
            pygame.display.update()
    

            
            
        