import pygame
import random

"""
    This file implements the ai cars
    Spawns them at random x and y cords near the top of the screen
    Go down at random speeds that reset everytime the
    bot makes it to the bottom of the screen
    Stefan Perkovic December 18 2023
"""

class Bot(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75

    def __init__(self, type):
        if type == "TRUCK":
            self.image = pygame.image.load("resources/truck.png")
        else:
            self.image = pygame.image.load("resources/enemies_car.png")

        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect_x = random.randint(50, 700)
        self.rect_y = random.randint(0, 50)
        self.speed = random.randint(5, 50) * 0.01

    def move_forward(self):
        self.reset()
        self.rect_y += self.speed

    # Resets the bot to a random position at the top of the screen
    def reset(self):
        if self.rect_y > 600:
            self.rect_x = random.randint(50, 700)
            self.rect_y = random.randint(0, 50)

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x , self.rect_y))
    