"""main.py

objects: screen, player, follower

TODO:
- simple objects for player sprite
- train constant speed
- player slows down
- lose on collision
- flat level"""

import pygame
import math

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

def main():
	pygame.init()
	screen = pygame.display.set_mode((640,480))

	running = True
	while running == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill(WHITE)

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()