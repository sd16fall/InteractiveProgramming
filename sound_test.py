import pygame
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("engines.mp3")
sounda.play()
pygame.event.wait()
