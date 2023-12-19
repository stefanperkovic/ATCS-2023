import pygame

"""
    This file implements the users cars
    

    Stefan Perkovic December 18 2023
"""

class Car(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75

    def __init__(self):
        self.velocity_x = 0.2
        self.velocity_y = 0.2
        self.image = pygame.image.load("resources/car.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect_x = 400
        self.rect_y = 500

    def pixel_perfect_collision(self, sprite1, sprite2):
        mask1 = pygame.mask.from_surface(sprite1.image)
        mask2 = pygame.mask.from_surface(sprite2.image)
        offset = (sprite2.rect_x - sprite1.rect_x, sprite2.rect_y - sprite1.rect_y)
        return mask1.overlap(mask2, offset)

    def move_up(self):
        self.rect_y -= self.velocity_y
    def move_down(self):
        self.rect_y += self.velocity_y
    def move_left(self):
        self.rect_x -= self.velocity_x
    def move_right(self):
        self.rect_x += self.velocity_x
        
    def speed_up(self):
        self.velocity_y = 0.4
        self.velocity_x = 0.4

    def slow_down(self):
        self.velocity_y = 0.1
        self.velocity_x = 0.1

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))


