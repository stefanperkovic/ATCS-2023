import pygame
import random


class Bot(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75

    def __init__(self, game):
        self.truck = pygame.image.load("resources/truck.png")
        self.truck = pygame.transform.scale(self.truck, (self.WIDTH, self.HEIGHT))
        # self.rect = self.truck.get_rect()
        self.rect_x = random.randint(50, 700)
        self.rect_y = random.randint(0, 50)
        # self.speed = random.randint(2, 5)
        self.speed = 0.1




    def move_forward(self):
        self.reset()
        self.rect_y += self.speed

    def reset(self):
        if self.rect_y > 600:
            self.rect_x = random.randint(50, 700)
            self.rect_y = random.randint(0, 50)



    def draw(self, screen):
        screen.blit(self.truck, (self.rect_x , self.rect_y))
    