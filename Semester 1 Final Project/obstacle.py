import pygame
import random
"""
    This file implements the two obstacles the user can encouter oil and ice
    These obstacles chagne the users current state affecting their movement
    Stefan Perkovic December 18 2023
"""
class Obstacle(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75
    
    def __init__(self, type):
        if type == "ICE":
            self.image = pygame.image.load("resources/waterspill.png")
        else:
            self.image = pygame.image.load("resources/oil.png")

        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect_x = random.randint(100, 650)
        self.rect_y = random.randint(150, 400)

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))
