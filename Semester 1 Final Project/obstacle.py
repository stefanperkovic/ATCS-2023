import pygame
import random



class Obstacle(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75
    
    def __init__(self, type):
        if type == "ICE":
            self.image = pygame.image.load("resources/waterspill.png")
            self.image = pygame.transform.scale(self.image, (75, 75))
        else:
            self.image = pygame.image.load("resources/oil.png")
            self.image = pygame.transform.scale(self.image, (75, 75))


        self.rect = self.image.get_rect()
        self.rect_x = random.randint(100, 650)
        self.rect_y = random.randint(150, 400)

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))
