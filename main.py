#
#	Created in 02/23/18
#	by Thais Luca
#

import pygame, sys, random, time
from constants import *
from gameFunctions import *

# Initializing Pygame
# returns a tuple. The first number is for successfully functions
# the second is the number of errors.
check_errors = pygame.init()
if check_errors[1] > 0:
	print "Found {0} initializing errors".format(check_errors[1])
	sys.exit(-1)
else:
	print "PyGame successfully initialized."

# Creating play surface
playSurface = pygame.display.set_mode((HEIGHT, WIDTH))

# Setting header
pygame.display.set_caption(HEADER)

# Creating frames per second controller
fpsController = pygame.time.Clock()


# Snake's position
snakePos = [100, 50]

# The snake starts with 3 blocks for its body
snakeBody = [[100,50],[90,50],[80,50]]

# Food position
foodPos = [random.randrange(1, HEIGHT/10)*10, random.randrange(1, WIDTH/10)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0

# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
 
    # validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
 
    # Update snake position [x,y]
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
   
   
    # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
       
    #Food Spawn
    if foodSpawn == False:
        foodPos = newFood()
    foodSpawn = True
   
    #Background
    playSurface.fill(black)
   
    #Draw Snake
    for block in snakeBody:
        pygame.draw.rect(playSurface, white, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
   
    pygame.draw.rect(playSurface, orange, pygame.Rect(foodPos[0], foodPos[1], BLOCK_SIZE, BLOCK_SIZE))
   
    # Bound
    if snakePos[0] > HEIGHT-BLOCK_SIZE or snakePos[0] < 0:
        gameOver(playSurface, score)
    if snakePos[1] > WIDTH-BLOCK_SIZE or snakePos[1] < 0:
        gameOver(playSurface, score)
       
    # Self hit
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver(playSurface, score)
   
    #common stuff
    showScore(1, score, playSurface)
    pygame.display.flip()
   
    fpsController.tick(24)
