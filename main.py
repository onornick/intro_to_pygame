#!/usr/bin/env python3
import pygame
from sys import exit
"""
This module contains the game loop which provides
the screen that displays everything
"""

pygame.init()
snail_x_pos = 800
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
snail_surface = pygame.image.load('graphics/snail/snail1.png')
font_surface = font.render('START...', False, 'Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(font_surface, (300, 50))
    snail_x_pos -= 2
    if snail_x_pos < -100: snail_x_pos = 800 
    screen.blit(snail_surface, (snail_x_pos, 265))

    pygame.display.update()
    clock.tick(60)
