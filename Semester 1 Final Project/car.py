import pygame
"""
    This file implements the users car
    Any imputs made in the game move the car here
    Car can either be in a normal, slow, or boost state
    If it hits oil it changes to slow and if it hits ice it changes to fast
    If it collides with another car or truck the game ends as there was a crash
    Stefan Perkovic December 18 2023
"""
class Car(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75
    INITIAL_VELOCITY = 0.2
    BOOST_VELOCITY = 0.4
    SLOW_VELOCITY = 0.1
    INITIAL_X = 400
    INITIAL_Y = 500
    

    def __init__(self):
        self.velocity_x = self.INITIAL_VELOCITY
        self.velocity_y = self.INITIAL_VELOCITY
        self.image = pygame.image.load("resources/car.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect_x = self.INITIAL_X
        self.rect_y = self.INITIAL_Y
    # Checks if the two line collide
    # Written by Chatgpt
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
    # Faster state of the car
    def speed_up(self):
        self.velocity_y = self.BOOST_VELOCITY
        self.velocity_x = self.BOOST_VELOCITY
    # Slower state of the car
    def slow_down(self):
        self.velocity_y = self.SLOW_VELOCITY
        self.velocity_x = self.SLOW_VELOCITY
    # Handles the user imput when the keys are held down
    # Written by Chatgpt
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


