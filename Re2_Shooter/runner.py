#!/bin/python

import pygame
import sys

pygame.init()

# Settings
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Resident Evil 2')
clock = pygame.time.Clock()
#font = pygame.font.Font('font/Pixeltype.ttf', 50)
#font_surf = font.render('Runner', False, 'black').convert()

# Environment
kendo_surf = pygame.image.load('graphics/kendos2.png').convert()
sidewalk_surf = pygame.image.load('graphics/sidewalk.png').convert()

# Sprites
claire_surf = pygame.image.load('graphics/Player/claire_standing.png').convert_alpha()
claire_rect = claire_surf.get_rect(midbottom = (100, 275))
scale_factor = 1.35
claire_surf = pygame.transform.scale(claire_surf, (int(claire_surf.get_width() * scale_factor), int(claire_surf.get_height() * scale_factor)))
claire_rect.size = claire_surf.get_size()  # Update the rect size to match the scaled image size

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(kendo_surf, (0,0))
    screen.blit(sidewalk_surf, (0, 299))
    screen.blit(claire_surf, claire_rect)
    
    clock.tick(60)
    pygame.display.update()
