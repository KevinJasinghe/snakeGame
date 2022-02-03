import pygame
import random
import time

pygame.init()  # initializes the game

width, height = 400, 400  # holds the width and height values
game_screen = pygame.display.set_mode((width, height))  # width and height of the game screen
pygame.display.set_caption("The Snake Game")  # title of the game

x, y = 200, 200  # initial coordinates of the snake
delta_x, delta_y = 10, 0  # upward and downward movement

clock = pygame.time.Clock()  # allows us to set up a frame rate

food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0,height) // 10 * 10  # random position of the food

body_list = [(x, y)]  # stores initial coord of the snake

game_over = False

font = pygame.font.SysFont("bahnschrift", 25)

def snake():
    global x, y, food_y, food_x, game_over
    x = (x + delta_x) % width  # moves the snake in the x dir (mod makes it come from the other side when it touches the end)
    y = (y + delta_y) % height  # moves the snake in the y dir (mod makes it come from the other side when it touches the end)

    if (x, y) in body_list:
        game_over = True
        return

    body_list.append((x, y))  # when the snake eats the food increases the length

    if food_x == x and food_y == y :  # when the snake comes in contact with the food
        while (food_x, food_y) in body_list:
            food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0,height) // 10 * 10
    else:
        del body_list[0]

    game_screen.fill((0, 0, 0))  # clears the screen (prevents duplication of the snake)
    score = font.render("Score: " + str(len(body_list)), True, (255, 255, 0))  # set up a score message
    game_screen.blit(score, [0, 0])  # display the message
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10])  # draws white rectangle on screen representing food
    for i, j in body_list:  # for ever coord in body list increase the size of the snake
        pygame.draw.rect(game_screen, (255, 255, 255), [i, j, 10, 10])  # draws the snake as a white rectangle
    pygame.display.update()  # updates the game screen


while True:  # ensures the game keeps on running
    if game_over:
        game_screen.fill((0, 0, 0))  # clears everything in the screen
        score = font.render("Score: " + str(len(body_list)), True, (255, 255, 0))  # set up a score message
        game_screen.blit(score, [0, 0])  # display the message
        msg = font.render("GAME OVER", True, (255, 255, 255))  # displays a game over message
        game_screen.blit(msg, [width//3, height//3])
        pygame.display.update()
        time.sleep(3) # stops the code for 3 seconds
        pygame.quit()  # stops the game
        quit()  # exits the program
    events = pygame.event.get()  # gets the events of pygame (everything in pygame is a event)
    for event in events:  # all the events run here
        if event.type == pygame.QUIT:  # if the event is the user clicking the close screen
            pygame.quit()  # stops the game
            quit()  # exits the program
        if event.type == pygame.KEYDOWN:  # when a key is held down
            if event.key == pygame.K_LEFT:  # when the left arrow key is pressed
                if delta_x != 10:  # only if the snake is not moving to the right already
                    delta_x = -10  # moves the snake 10 to the left
                delta_y = 0  # no movement up or down
            elif event.key == pygame.K_RIGHT:
                if delta_x != -10:  # only if the snake is not moving to the left already
                    delta_x = 10  # moves the snake 10 to the right
                delta_y = 0  # no movement up or down
            elif event.key == pygame.K_UP:
                delta_x = 0  # no movement left or right
                if delta_y != 10:  # only if the snake is not moving down already
                    delta_y = -10  # moves the snake 10 up
            elif event.key == pygame.K_DOWN:
                delta_x = 0  # no movement left or right
                if delta_y != 10:  # only if the snake is not moving up already
                    delta_y = 10  # moves the snake 10 down
            else:
                continue
            snake()  # called after every key pressed

    if not events:
        snake()  # will be called even if there is no event (makes the snake move in even when button not pressed)
    clock.tick(10)  # adding the frame rate
