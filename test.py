
import pygame
import sys
import time
import random


pygame.init()


white = (255,255,255)
grey = (155,155,155)

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
dark_green = (0,55,0)

blue = (0,0,100)

clock = pygame.time.Clock()

display_width = 1200
display_height = 800
block_size = 10
FPS = 15
rand_size = 30
direction = "down"

img = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/arrow.png")
apple = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/apple.png")
icon = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/apple.png")

smallfont = pygame.font.SysFont("helvetica", 25)
medfont = pygame.font.SysFont("helvetica", 50)
largefont = pygame.font.SysFont("helvetica", 80)

def snake(block_size, snakelist, direction):


    if direction == "down":
        head = pygame.transform.rotate(img, 270)
        head = pygame.transform.scale(head, (block_size, block_size))
    if direction == "up":
        head = pygame.transform.rotate(img, 90)
        head = pygame.transform.scale(head, (block_size, block_size))
    if direction == "right":
        head = pygame.transform.rotate(img, 0)
        head = pygame.transform.scale(head, (block_size, block_size))
    if direction == "left":
        head = pygame.transform.rotate(img, 180)
        head = pygame.transform.scale(head, (block_size, block_size))

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])





def text_objects(text, colour, size):

    if size == "small":
        textSurface = smallfont.render(text, True, colour)
    elif size == "medium":
        textSurface = medfont.render(text, True, colour)
    elif size == "large":
        textSurface = largefont.render(text, True, colour)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, colour, y_adjust=0, size = "small"):
    textSurf, textRect = text_objects(msg, colour, size)
    textRect.center = (display_width/2), (display_height/2) - y_adjust
    gameDisplay.blit(textSurf, textRect)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither")
pygame.display.set_icon(icon)


def rand_dot():
    rand_dot_x = random.randrange(block_size, display_width - rand_size - block_size)#/block_size - 2)*block_size
    rand_dot_y = random.randrange(block_size, display_height - rand_size - block_size)#/block_size - 2)*block_size
    return rand_dot_x, rand_dot_y

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [block_size, block_size])


def game_intro():
    lead_colour = "black"
    gameExit = False
    gameOver = False
    gamePause = False
    gameStart = True


    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = block_size
    rand_dot_x, rand_dot_y = rand_dot()
    direction = "down"

    snakelist = []

    snake_len = 1
    while gameStart:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  ##quit game
                gamePause = False
                gameExit = True
                gameStart = False

                gameDisplay.fill(grey)
                pygame.draw.rect(gameDisplay, dark_green, [0, 0, block_size, display_height])
                pygame.draw.rect(gameDisplay, dark_green, [0, 0, display_width, block_size])
                pygame.draw.rect(gameDisplay, dark_green, [0, display_height - block_size, display_width, block_size])
                pygame.draw.rect(gameDisplay, dark_green, [display_width - block_size, 0, block_size, display_height])
                message_to_screen("Quiting game", black)
                pygame.display.update()

                time.sleep(2)

                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameExit = True
                    gamePause = False
                    gameStart = False
                    gameDisplay.fill(grey)
                    pygame.draw.rect(gameDisplay, dark_green, [0, 0, block_size, display_height])
                    pygame.draw.rect(gameDisplay, dark_green, [0, 0, display_width, block_size])
                    pygame.draw.rect(gameDisplay, dark_green, [0, display_height - block_size, display_width, block_size])
                    pygame.draw.rect(gameDisplay, dark_green, [display_width - block_size, 0, block_size, display_height])
                    message_to_screen("Quiting game", black)
                    pygame.display.update()

                    time.sleep(2)

                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    gamePause = False
                    gameStart = False
                    lead_x = display_width / 2
                    lead_y = display_height / 2
                    lead_x_change = 0
                    lead_y_change = block_size
                    rand_dot_x = random.randrange(1, display_width - 2 * block_size)  # /block_size - 2)*block_size
                    rand_dot_y = random.randrange(1, display_height - 2 * block_size)  # /block_size - 2)*block_size
                    snakelist = []
                    direction = "down"
                    snake_len = 1

                elif event.key == pygame.K_SPACE:
                    gamePause = False
                    gameStart = False

                elif event.key == pygame.K_ESCAPE:
                    gameStart = False
                    gamePause = False
                    gameExit = True
                    gameDisplay.fill(grey)
                    pygame.draw.rect(gameDisplay, dark_green, [0, 0, block_size, display_height])
                    pygame.draw.rect(gameDisplay, dark_green, [0, 0, display_width, block_size])
                    pygame.draw.rect(gameDisplay, dark_green, [0, display_height - block_size, display_width, block_size])
                    pygame.draw.rect(gameDisplay, dark_green, [display_width - block_size, 0, block_size, display_height])
                    message_to_screen("Quiting game", black)

                    pygame.display.update()

                    time.sleep(2)

                    pygame.quit()
                    sys.exit()

        gameDisplay.fill(grey)
        pygame.draw.rect(gameDisplay, dark_green, [0, 0, block_size, display_height])
        pygame.draw.rect(gameDisplay, dark_green, [0, 0, display_width, block_size])
        pygame.draw.rect(gameDisplay, dark_green, [0, display_height - block_size, display_width, block_size])
        pygame.draw.rect(gameDisplay, dark_green, [display_width - block_size, 0, block_size, display_height])
        message_to_screen("Welcome!", blue, y_adjust = 100, size="large")
        message_to_screen("Collect the apples while avoiding", black, size="medium", y_adjust=30)
        message_to_screen("the walls and don't run into your tail!", black, size="medium", y_adjust=-30)
        message_to_screen("Press Spacerbar to start", black, y_adjust = -80)
        pygame.display.update()

        clock.tick(5)

def gameLoop():
    lead_colour = "black"
    gameExit = False
    gameOver = False
    gamePause = False
    gameStart = True


    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = block_size
    rand_dot_x, rand_dot_y = rand_dot()

    direction = "down"

    snakelist = []

    snake_len = 1

    while not gameExit:
        while gameOver == True:
            message_to_screen("Game Over", red, y_adjust=50, size="large")
            message_to_screen("Press Spacerbar to play again or Q to quit.", black)
            pygame.display.update()
            clock.tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  ##quit game
                    gameOver = False
                    gameExit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_SPACE:
                        gameOver = False
                        lead_x = display_width / 2
                        lead_y = display_height / 2
                        lead_x_change = 0
                        lead_y_change = block_size
                        rand_dot_x, rand_dot_y = rand_dot()

                        snakelist = []
                        direction = "down"
                        snake_len = 1
                    elif event.key == pygame.K_ESCAPE:
                        gameOver = False
                        gameExit = True



        while gamePause == True:
            message_to_screen("Game Paused!", blue, y_adjust=50, size="large")
            message_to_screen("Press Spacerbar to continue or P to play again.", black)
            pygame.display.update()
            clock.tick(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  ##quit game
                    gamePause = False
                    gameExit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gamePause = False
                    elif event.key == pygame.K_p:
                        gamePause = False
                        gameStart = False
                        lead_x = display_width / 2
                        lead_y = display_height / 2
                        lead_x_change = 0
                        lead_y_change = block_size
                        rand_dot_x, rand_dot_y = rand_dot()

                        snakelist = []
                        direction = "down"
                        snake_len = 1

                    elif event.key == pygame.K_SPACE:
                        gamePause = False
                        gameStart = False

                    elif event.key == pygame.K_ESCAPE:
                        gamePause = False
                        gameExit = True

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:##quit game
                gameOver = False
                gameExit = True
            elif event.type == pygame.KEYDOWN:##start movements
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
                elif event.key == pygame.K_ESCAPE:
                    gameOver = False
                    gameExit = True
                elif event.key == pygame.K_SPACE:
                    gamePause = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #lead_x_change = 0
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    #lead_y_change = 0
                    pass

        lead_x += lead_x_change
        lead_y += lead_y_change
        if gamePause == False:


            if lead_x >= rand_dot_x and lead_x < rand_dot_x + rand_size:
                if lead_y >= rand_dot_y and lead_y < rand_dot_y + rand_size:
                    rand_dot_x, rand_dot_y = rand_dot()

                    snake_len += 1
            if lead_x + block_size >= rand_dot_x and lead_x + block_size < rand_dot_x + rand_size:
                if lead_y + block_size >= rand_dot_y and lead_y + block_size < rand_dot_y + rand_size:
                    rand_dot_x, rand_dot_y = rand_dot()

                    snake_len += 1
            if lead_x > rand_dot_x and lead_x < rand_dot_x + rand_size or lead_x + block_size > rand_dot_x and lead_x + block_size < rand_dot_x + rand_size or lead_x < rand_dot_x and lead_x + block_size > rand_dot_x or lead_x < rand_dot_x + rand_size and lead_x + block_size > rand_dot_x  + rand_size:
                if lead_y > rand_dot_y and lead_y < rand_dot_y + rand_size or lead_y + block_size > rand_dot_y and lead_y + block_size < rand_dot_y + rand_size or lead_y < rand_dot_y and lead_y + block_size > rand_dot_y or lead_y < rand_dot_y + rand_size and lead_y + block_size > rand_dot_y + rand_size:
                    rand_dot_x, rand_dot_y = rand_dot()

                    snake_len += 1



            if lead_x >= display_width - block_size or lead_x <= 0 or lead_y >= display_height - block_size or lead_y <= 0:
                gameOver = True
            gameDisplay.fill(grey)
            pygame.draw.rect(gameDisplay, dark_green, [0, 0, block_size, display_height])
            pygame.draw.rect(gameDisplay, dark_green, [0, 0, display_width, block_size])
            pygame.draw.rect(gameDisplay, dark_green, [0, display_height - block_size, display_width, block_size])
            pygame.draw.rect(gameDisplay, dark_green, [display_width - block_size, 0, block_size, display_height])


            # pygame.draw.rect(gameDisplay, red, [rand_dot_x, rand_dot_y, rand_size, rand_size])
            gameDisplay.blit(apple, (rand_dot_x, rand_dot_y))

            snakeHead = []
            snakeHead.append(lead_x)
            snakeHead.append(lead_y)
            if snakeHead in snakelist:
                gameOver = True

            snakelist.append(snakeHead)
            if(len(snakelist) > snake_len):
                del snakelist[0]


            snake(block_size, snakelist, direction)

            score(snake_len - 1)
        pygame.display.update()

        clock.tick(FPS)

game_intro()
gameLoop()

message_to_screen("Quiting game", black)
pygame.display.update()

time.sleep(2)

pygame.quit()
sys.exit()