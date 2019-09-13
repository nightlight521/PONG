#########################################
# File Name: BrickBreakerStarter.py
# Description: Starter code for Brick Breaker game
# Author: ICS2O
# Date: 08/11/2017
#########################################
import pygame
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
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
outline = 0

#---------------------------------------#
# functions                             #
#---------------------------------------#
def redrawGameWindow():
    gameWindow.fill(BLACK)
    pygame.draw.circle(gameWindow, WHITE, (ballX, ballY), ballR, outline)
    pygame.draw.rect(gameWindow, GREEN, (paddleX, paddleY, paddleW, paddleH), outline)
    pygame.draw.rect(gameWindow, BLUE, (brickX, brickY, brickW, brickH), outline)
    pygame.display.update()
        
#---------------------------------------#
# main program                          #
#---------------------------------------#
print "Hit ESC to end the program."

# ball properties
ballR  = 25
ballX  =  WIDTH/2
ballY  =  2*ballR
speedX =  1
speedY =  1

# paddle properties 
paddleW  = 120
paddleH  = 20
paddleX = (WIDTH - paddleW)/2
paddleY = BOTTOM - paddleH/2
paddleShift = 2

# brick properties
brickW = 100
brickH = 30
brickX = 150
brickY = 10

inPlay = True
while inPlay:
    redrawGameWindow()
    pygame.time.delay(2)
    
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_LEFT]:
        paddleX = paddleX - paddleShift
    if keys[pygame.K_RIGHT]:
        paddleX = paddleX + paddleShift

# bounce the ball from the paddle
    if ballX >= paddleX and ballX <= paddleX+paddleW and ballY+ballR >= paddleY:
        speedY = -speedY
# bounce the ball from the brick
    if ballX >= brickX and ballX <= brickX+brickW and ballY-ballR <= brickY+brickH:
        speedY = -speedY
# bounce the ball from left, right, and top borders
    if ballX>= RIGHT or ballX<=LEFT:
        speedX = -speedX
    if ballY<=TOP:
        speedY = -speedY
# move the ball
    ballX = ballX + speedX
    ballY = ballY + speedY    
    if ballY+ballR > BOTTOM:
        print "Game Over!"
        inPlay = False
        
#---------------------------------------# 
pygame.quit()
