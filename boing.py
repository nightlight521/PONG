#########################################
# File Name: Hungry Pong
# Description: Pong Assignment
# Author: Paula Yuan and Rachel Kim
# Date: 0ct. 31, 2018   
#########################################
import pygame
import time
from random import choice
from random import randint

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

TOP    = 0  
BOTTOM = HEIGHT
LEFT   = 0     
RIGHT  = WIDTH 
GREEN = (  0,255,  0)
BLUE  = (  0,  0,128)
BRIGHTBLUE =(82, 239, 255)
BRIGHTRED = (242, 51, 51)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
GREY =(80, 80, 80)
outline = 0

#---------------------------------------#
# functions                             #
#---------------------------------------#
def drawText(font, text, colour, x, y):
    graphics = font.render(text, 1, colour)
    gameWindow.blit(graphics, (x, y))

def redrawCookieMonsterWindow():
    gameWindow.fill(BLACK)
    gameWindow.blit(bkgd, (0, 0))
    pygame.draw.line(gameWindow, WHITE, (400, 0), (400, 600), 3)
    gameWindow.blit(cookie, (ballX-25, ballY-25))
    pygame.draw.rect(gameWindow, BRIGHTRED, (padX, padY, padW, padH), outline)
    pygame.draw.rect(gameWindow, BRIGHTBLUE, (pad2X, pad2Y, pad2W, pad2H), outline)
    drawText(smallFont, "Guest: "+str(guestScore), WHITE, 680, 30)
    drawText(smallFont, "Home: "+str(homeScore), WHITE, 30, 30)
    pygame.display.update()

def drawSpeedRect():
    pygame.draw.rect(gameWindow,WHITE,(195,290,45,40),2)
    pygame.draw.rect(gameWindow,WHITE,(345,290,70,40),2)
    pygame.draw.rect(gameWindow,WHITE,(505,290,50,40),2)
    if speed == 4:
        pygame.draw.rect(gameWindow,BRIGHTBLUE,(195,290,45,40),2)
    if speed == 6:
        pygame.draw.rect(gameWindow,BRIGHTBLUE,(345,290,70,40),2)
    if speed == 8:
        pygame.draw.rect(gameWindow,BRIGHTBLUE,(505,290,50,40),2)

def drawMenu():
    gameWindow.blit(menuBkgd, (0,0))
    drawText(bigFont, "HUNGRY PONG", WHITE, 230, 100)
    drawText(smallFont, "WASD for Home player, arrow keys (up down left right) for Guest. First to get to 7 points wins!", WHITE, 50, 200)
    drawText(smallFont, "Choose your level of difficulty:", WHITE, 260, 250)
    drawText(smallFont, "EASY", WHITE, 200, 300)
    drawText(smallFont, "MEDIUM", WHITE, 350, 300)
    drawText(smallFont, "HARD", WHITE, 510, 300)
    drawText(smallFont, "To pause the game, press 'p'.", WHITE, 280, 360)
    drawText(medFont, "PRESS SPACEBAR TO START", BRIGHTBLUE, 230, 440)
    drawSpeedRect()
    pygame.display.update()

def drawPauseMenu():
    gameWindow.blit(pauseBkgd, (0, 0))
    drawText(bigFont, "PAUSED", WHITE, 320, 130)
    drawText(smallFont, "Psst. Are you hungry yet? I am.", WHITE, 290, 400)
    drawText(smallFont, "Press U to Unpause. Now give us a cookie because we let you unpause.", WHITE, 150, 450)
    pygame.display.update()

def drawEndMenu():
    gameWindow.blit(endBkgd, (0,0))
    pygame.draw.rect(gameWindow, WHITE, (170, 270, 525, 170))
    drawText(bigFont, "GAME OVER", BLACK, 270, 280)
    if homeWin:
        drawText(medFont, "WINNER: HOME", BLACK, 310, 350)
    elif guestWin:
        drawText(medFont, "WINNER: GUEST", BLACK, 310, 350)
    drawText(smallFont, "Hope you're sick of cookies now. (Press Esc to close the game.)", BLACK, 180, 400)
    pygame.display.update()

def playMenuSong():
    pygame.mixer.music.load("bouncysong.ogg")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

def playMainSong():
    pygame.mixer.music.load("windfall.ogg")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

def playBoing():
    boing.set_volume(0.5)
    boing.play(0)
    
def playMunch():
    munch.set_volume(0.5)
    munch.play(0)
                    
#---------------------------------------#
# define variables                      #
#---------------------------------------#
print "Hit ESC to end the program."

# standard speed
speed = 6

# ball properties
ballR  = WIDTH/32
ballX  = WIDTH/2
ballY  = 10*ballR

# pad 1 properties 
padW  = WIDTH/40
padH  = HEIGHT/5
padX = LEFT + 5
padY = TOP + HEIGHT/2 - padH/2
PAD_SHIFT = 5

# pad 2 properties
pad2W = WIDTH/40
pad2H = HEIGHT/5
pad2X = RIGHT - pad2W - 5
pad2Y = TOP + HEIGHT/2 - pad2H/2

# Scoring
guestScore = 0
homeScore = 0
WIN_SCORE = 7

# Cheating
cheatPressed = False
cheated = False

# Pausing
pause = False
recommence = False

# Exiting Game
giveUp = False

# Time
clock = pygame.time.Clock()
FPS = 70
PERIOD = 1
BEGIN = time.time()
referenceTime = BEGIN
elapsed = 0
waiting = False 

#-----------------------------#
# Images, sound effects, font #
#-----------------------------#

#images
bkgd = pygame.image.load("cookiemonster.png").convert()
pauseBkgd = pygame.image.load("cookiemonster1.jpg").convert()
menuBkgd = pygame.image.load("star.png").convert()
endBkgd = pygame.image.load("wave.jpg").convert()
cookie = pygame.image.load("cookie.png")

#sound effects
munch = pygame.mixer.Sound("Munch.wav")
boing = pygame.mixer.Sound("Boing.wav")

#font
smallFont = pygame.font.SysFont("Impact", 18)
medFont = pygame.font.SysFont("Impact", 30)
bigFont = pygame.font.SysFont("Impact", 60)

#-------------------------------#
# main program                  #
#-------------------------------#

#play menu music
playMenuSong()
    
#display menu
showMenu = True
while showMenu:
    drawMenu()
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        showMenu = False

    mouseX,mouseY = pygame.mouse.get_pos()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and mouseX >=195 and mouseX <=240 and mouseY >=290 and mouseY <=330:
            speed = 4
        elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >=345 and mouseX <=415 and mouseY >=290 and mouseY <=330:
            speed = 6
        elif event.type == pygame.MOUSEBUTTONDOWN and mouseX >=505 and mouseX <=555 and mouseY >=290 and mouseY <=330:
            speed = 8

#stop menu music, load and play main game music        
pygame.mixer.music.stop()
playMainSong()

speedX = choice((speed, -speed))
speedY = speed

#start game
clock.tick(2)

inPlay = True
while inPlay:
    pygame.event.clear()
    if not pause:
        redrawCookieMonsterWindow()
        if recommence:
            clock.tick(1)
            recommence = False
    clock.tick(FPS)

    keys = pygame.key.get_pressed()

    # to exit game
    if keys[pygame.K_ESCAPE]:
        giveUp = True
        inPlay = False

   # pause menu stuff
    if keys[pygame.K_p]:
        pause = True
    if pause:
        if speedX != 0 and speedY != 0:
            prevSpeedX, prevSpeedY = speedX, speedY
        speedX, speedY,  = 0, 0, 0
        drawPauseMenu()
        keys = pygame.key.get_pressed()
    if keys[pygame.K_u] and pause:
        pause = False
        speedX, speedY, PAD_SHIFT = prevSpeedX, prevSpeedY, 5
        recommence = True

    # keyboard stuff
    if keys[pygame.K_w] and padY > 0:
        padY = padY - PAD_SHIFT
    if keys[pygame.K_s] and padY+padH < 600:
        padY = padY + PAD_SHIFT

    if keys[pygame.K_a] or keys[pygame.K_d] and cheated == False:            # cheat
        cheatPressed = True
        cheated = True
    if cheatPressed:
        if keys[pygame.K_LEFT] and pad2Y > 0:
            pad2Y = pad2Y - PAD_SHIFT
        if keys[pygame.K_RIGHT] and pad2Y+pad2H < 600:
            pad2Y = pad2Y + PAD_SHIFT
    else:
        if keys[pygame.K_UP] and pad2Y > 0:
            pad2Y = pad2Y - PAD_SHIFT
        if keys[pygame.K_DOWN] and pad2Y+pad2H < 600:
            pad2Y = pad2Y + PAD_SHIFT
   
    # keep track of the score
    if ballX-ballR <= LEFT-2*ballR:
        playMunch()
        guestScore = guestScore + 1
        if cheatPressed == True:
            cheatPressed = False 
        ballX = WIDTH/2
        ballY = randint(50, 550)
        speedX = -speedX
        speedY = choice((speedY, -speedY))
        waiting = True
        referenceTime = time.time()
    elapsed = round(time.time() - referenceTime, 1)
    if ballX+ballR >= RIGHT+2*ballR:
        playMunch()
        if cheatPressed == True:
            cheatPressed = False 
        homeScore = homeScore + 1
        ballX = WIDTH/2
        ballY = randint(50, 550)
        speedX = -speedX
        speedY = choice((speedY, -speedY))
        waiting = True
        referenceTime = time.time()   
    elapsed = round(time.time() - referenceTime, 1)
    if elapsed > PERIOD:
        waiting = False
                
# bounce the ball from the pad
    if ballX-ballR < padX+padW and ballY+ballR >= padY and ballY-ballR <= padY+padH:
        ballX = padX+padW+ballR
    if ballX-ballR == padX+padW and ballY+ballR >= padY and ballY-ballR <= padY+padH:
        playBoing()
        speedX = -speedX
# bounce the ball from the second pad
    if ballX+ballR > pad2X and ballY+ballR >= pad2Y and ballY-ballR <= pad2Y+pad2H:
        ballX = pad2X-ballR
    if ballX+ballR == pad2X and ballY+ballR >= pad2Y and ballY-ballR <= pad2Y+pad2H:
        playBoing()
        speedX = -speedX
# bounce the ball from top and bottom borders
    if ballY-ballR<=TOP or ballY+ballR >= BOTTOM:
        speedY = -speedY

# move the ball
    if not waiting:    
        ballX = ballX + speedX
        ballY = ballY + speedY

# End the game
    if homeScore == WIN_SCORE:
        redrawCookieMonsterWindow()
        clock.tick(FPS)
        homeWin = True
        inPlay = False
    if guestScore == WIN_SCORE:
        redrawCookieMonsterWindow()
        clock.tick(FPS)
        guestWin = True
        homeWin = False
        inPlay = False

while not giveUp:
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    drawEndMenu()
    if keys[pygame.K_ESCAPE]:
       giveUp = True
        
#---------------------------------------# 
pygame.quit()
