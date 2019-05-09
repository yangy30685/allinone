import pygame
from pygame.locals import *
from sys import exit

background_image = 'C:\\Users\\Administrator\\Documents\\GitHub\\allinone\\python\\app_2\\pic.gif'
mouse_image = ''

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('hello world')

background = pygame.image.load(background_image.convert())
mouse = pygame.image.load(mouse_image).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT
            exit()
    screen.blit(background, (0, 0))

    x, y = pygame.mouse.get_pos()

    x -= mouse_cursor.get_width()/2
    y -= 