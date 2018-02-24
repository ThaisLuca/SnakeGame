#
#	Created at 02/23/18
#	by Thais Luca
#

import pygame, sys, random, time
from variables import *

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



# Game Over function
def gameOver():
	font = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)
	GOsurf = font.render(GAME_OVER, True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (HEIGHT/2, 15)
	playSurface.blit(GOsurf, GOrect)
	pygame.display.flip()


gameOver()
time.sleep(10)