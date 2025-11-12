import pygame

pygame.init()
sc = pygame.display.set_mode((800, 600))

bg = pygame.image.load('assets/img.png')

motor = pygame.image.load('assets/motor.png')

sc.blit(bg, (0, 0))
pygame.display.update()
pygame.display.flip()