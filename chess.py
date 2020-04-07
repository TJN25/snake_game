
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
display_width = 800
display_height = 800
smallfont = pygame.font.SysFont("helvetica", 25)
medfont = pygame.font.SysFont("helvetica", 50)
largefont = pygame.font.SysFont("helvetica", 80)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Chess")
img = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/Chess_Board.png")

wRook = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/white_rook.png")
wBishop = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/white_bishop.png")
wKing = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/white_king.png")
wQueen = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/white_queen.png")
wPawn = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/white_pawn.png")
wKnight = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/white_knight.png")
bRook = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/black_rook.png")
bBishop = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/black_bishop.png")
bKing = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/black_king.png")
bQueen = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/black_queen.png")
bPawn = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/black_pawn.png")
bKnight = pygame.image.load("/Users/thomasnicholson25/Desktop/py_charm_test/black_knight.png")

head = pygame.transform.scale(img, (700, 700))

wRook_head = pygame.transform.scale(wRook, (80, 80))
bRook_head = pygame.transform.scale(bRook, (80, 80))

wBishop_head = pygame.transform.scale(wBishop, (80, 80))
bBishop_head = pygame.transform.scale(bBishop, (80, 80))

wPawn_head = pygame.transform.scale(wPawn, (80, 80))
bPawn_head = pygame.transform.scale(bPawn, (80, 80))

wKing_head = pygame.transform.scale(wKing, (80, 80))
bKing_head = pygame.transform.scale(bKing, (80, 80))

wQueen_head = pygame.transform.scale(wQueen, (80, 80))
bQueen_head = pygame.transform.scale(bQueen, (80, 80))

wKnight_head = pygame.transform.scale(wKnight, (80, 80))
bKnight_head = pygame.transform.scale(bKnight, (80, 80))

width = [665, 575, 488, 401, 318, 230, 145, 55]
height = [55, 145, 230, 318, 401, 488, 575, 665]


d = {"wr1" : [0, 0, "wRook"],
"wk1" : [0, 1, "wKnight"],
"wb1" : [0, 2, "wBishop"],
"wQ" : [3, 4, "wQueen"],
"wK" : [0, 4, "wKing"],
"wb2" : [0, 5, "wBishop"],
"wk2" : [0, 6, "wKnight"],
"wr2" : [0, 7, "wRook"],
"wp1" : [1, 0, "wPawn"],
"wp2" : [1, 1, "wPawn"],
"wp3" : [1, 2, "wPawn"],
"wp4" : [1, 3, "wPawn"],
"wp5" : [1, 4, "wPawn"],
"wp6" : [1, 5, "wPawn"],
"wp7" : [1, 6, "wPawn"],
"wp8" : [1, 7, "wPawn"]}



def draw_pieces(d):
    for k,v in d.items():
        y= v[0]
        x=v[1]

        if v[2] == "wRook":
            gameDisplay.blit(wRook_head, (height[x], width[y]))
        elif v[2] == "wKnight":
            gameDisplay.blit(wKnight_head, (height[x], width[y]))
        elif v[2] == "wQueen":
            gameDisplay.blit(wQueen_head, (height[x], width[y]))
        elif v[2] == "wKing":
            gameDisplay.blit(wKing_head, (height[x], width[y]))
        elif v[2] == "wBishop":
            gameDisplay.blit(wBishop_head, (height[x], width[y]))
        elif v[2] == "wPawn":
            gameDisplay.blit(wPawn_head, (height[x] - 6, width[y]))

def move_piece(d, piece_select_x, piece_select_y):
    movePiece = True
    while movePiece:
        for k,v in d.items():
            if v[0] == piece_select_y and v[1] == piece_select_x:
                print(v[0])
                print(v[1])
                for event in pygame.event.get():
                    if event.key == pygame.K_LEFT:
                        if d[k][1] > 0:
                            d[k][1] -= 1
                            piece_select_x -= 1
                        else:
                            pass
                    elif event.key == pygame.K_RIGHT:
                        if d[k][1] < 7:
                            d[k][1] += 1
                            piece_select_x += 1
                        else:
                            pass
                    elif event.key == pygame.K_DOWN:
                        if d[k][0] > 0:
                            d[k][0] -= 1
                            piece_select_y -= 1
                        else:
                            pass
                    elif event.key == pygame.K_UP:
                        if d[k][0] < 7:
                            d[k][0] += 1
                            piece_select_y += 1
                        else:
                            pass
                    elif event.key == pygame.K_SPACE:
                        movePiece = False
                print(v[0])
                print(v[1])
        gameDisplay.fill(grey)

        gameDisplay.blit(head, (50, 50))

        draw_pieces(d)
        pygame.draw.rect(gameDisplay, black, [height[piece_select_x], width[piece_select_y], 15, 15])
        pygame.display.update()
        clock.tick(1)


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

piece_select_x = 0
piece_select_y = 0

gameExit = False
while not gameExit:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  ##quit game
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameExit = True
            elif event.key == pygame.K_ESCAPE:
                gameExit = True
            elif event.key == pygame.K_LEFT:
                if piece_select_x > 0:
                    piece_select_x -=  1
                else:
                    pass
            elif event.key == pygame.K_RIGHT:
                if piece_select_x < 7:
                    piece_select_x += 1
                else:
                    pass
            elif event.key == pygame.K_DOWN:
                if piece_select_y > 0:
                    piece_select_y -= 1
                else:
                    pass
            elif event.key == pygame.K_UP:
                if piece_select_y < 7:
                    piece_select_y += 1
                else:
                    pass
            elif event.key == pygame.K_SPACE:
                move_piece(d, piece_select_x, piece_select_y)

    gameDisplay.fill(grey)




    gameDisplay.blit(head, (50,50))




    draw_pieces(d)

    pygame.draw.rect(gameDisplay, black, [height[piece_select_x], width[piece_select_y], 15, 15])

    pygame.display.update()

    clock.tick(15)





message_to_screen("Quiting game", black, y_adjust= -375)
pygame.display.update()

time.sleep(2)


pygame.quit()
sys.exit()