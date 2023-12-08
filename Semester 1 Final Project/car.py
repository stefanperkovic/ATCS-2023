# Stefan Perkovic
import pygame


class Car(pygame.sprite.Sprite):
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, game):
        self.x = 100
        self.y_ = 100
        self.velocity_x = 0
        self.velocity_y = 0
        self.image = pygame.image.load("resources/car.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()

    def move_up(self):
        self.y += velocity_y
    def move_down(self):
        self.y -= velocity_y
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10

    def speed_up(self):
        self.velocity_y += 10

    def slow_down(self):
        self.velocity_y -= 10


    def init_fsm(self):
        # Add State Transitions
        states = ["NORMAL", "SLOW", "BOOST"]
        actions = [self.slow_down, self.speed_up]

        self.fsm.add_transition("OIL", "NORMAL", self.slow_down, "SLOW")
        self.fsm.add_transition("OIL", "SLOW", self.slow_down, "SLOW")
        self.fsm.add_transition("OIL", "BOOST", self.slow_down, "SLOW")

        self.fsm.add_transition("ICE" )

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))


