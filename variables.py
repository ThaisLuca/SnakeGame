
import random, pygame

HEIGHT = 720
WIDTH = 460
FONT_SIZE = 72
FONT_TYPE = 'monaco'
HEADER = 'Snake Game'
GAME_OVER = 'GAME OVER'

red = pygame.Color(178, 034, 034) # GAME OVER
black = pygame.Color(0, 0, 0) # BACKGROUND
white = pygame.Color(255, 255, 255) # SNAKE + SCORE
orange = pygame.Color(255, 140, 0) # FOOD

# Snake's position
snakePos = [100, 50]

# The snake starts with 3 blocks for its body
snakeBody = [[100,50],[90,50],[80,50]]

# Food position
foodPos = [random.randrange(1, HEIGHT/10)*10, random.randrange(1, WIDTH/10)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction