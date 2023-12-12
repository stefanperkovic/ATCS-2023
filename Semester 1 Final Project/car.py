# Stefan Perkovic
import pygame


class Car(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75

    def __init__(self, game):
        self.velocity_x = 0.1
        self.velocity_y = 0.1
        self.image = pygame.image.load("resources/car.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        # self.rect = self.image.get_rect()
        self.rect_x = 100
        self.rect_y = 500


    def move_up(self):
        self.rect_y -= self.velocity_y
    def move_down(self):
        self.rect_y += self.velocity_y
    def move_left(self):
        self.rect_x -= self.velocity_x
    def move_right(self):
        self.rect_x += self.velocity_x
        

    def speed_up(self):
        self.velocity_y += 10

    def slow_down(self):
        self.velocity_y -= 10


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


    def init_fsm(self):
        # Add State Transitions
        states = ["NORMAL", "SLOW", "BOOST"]
        actions = [self.slow_down, self.speed_up]

        self.fsm.add_transition("OIL", "NORMAL", self.slow_down, "SLOW")
        self.fsm.add_transition("OIL", "SLOW", self.slow_down, "SLOW")
        self.fsm.add_transition("OIL", "BOOST", self.slow_down, "SLOW")

        self.fsm.add_transition("ICE" )

    def draw(self, screen):
        screen.blit(self.image, (self.rect_x, self.rect_y))


