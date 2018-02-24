
import pygame, sys, time
from constants import *

# Game Over function
def gameOver(playSurface, score):
	font = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)
	GOsurf = font.render(GAME_OVER, True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (HEIGHT/2, 15)
	playSurface.blit(GOsurf, GOrect)
	showScore(0, score, playSurface)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit()
	sys.exit()


def newFood():
	return [random.randrange(1, HEIGHT/10)*10, random.randrange(1, WIDTH/10)*10] 

def showScore(choice, score, playSurface):
	font = pygame.font.SysFont(FONT_TYPE, SCORE_FONT_SIZE)
	Ssurf = font.render('Score: {0}'.format(score), True, white)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (80, 30)
	else:	
		Srect.midtop = ((HEIGHT/2), 120)
	playSurface.blit(Ssurf, Srect)
	pygame.display.flip()
	
