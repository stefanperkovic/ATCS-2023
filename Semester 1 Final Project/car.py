# Stefan Perkovic
import pygame


class Car:
    WIDTH = 50
    HEIGHT = 50

    def __init__(self):
        self.x = 100
        self.y_ = 100
        self.velocity_x = 0
        self.velocity_y = 0
        self.image = 
        self.car = pygame.image.load("car.png")
        self.car = pygame.transform.scale(self.car, (self.WIDTH, self.HEIGHT))

    def move_up(self):
        self.y += 10
    def move_down(self):
        self.y -= 10
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10


    def car.draw(self):


