import pygame
import random



class Obstacle(pygame.sprite.Sprite):
    WIDTH = 75
    HEIGHT = 75
    
    def __init__(self, type):
        if type == "ICE":
            self.image = pygame.image.load("resources/waterspill.jpeg")
            self.image = pygame.transform.scale(self.image, (75, 75))
        else:
            self.image = pygame.image.load("resources/oil.jpeg")
            self.image = pygame.transform.scale(self.image, (75, 75))


        self.rect = self.image.get_rect()
        self.rect_x = random.randint(50, 750)
        self.rect_y = random.randint(50, 550)



    def draw(self, screen):
        # self.num = random.randint(0, 1)
        # if self.num == 0:
        #     self.screen.blit(self.oil, (random.randint(50, 750), random.randint(50, 550)))
        #     self.screen.blit(self.oil, (100, 100))
        # # elif self.num == 1:
        #     # self.screen.blit(self.ice, (random.randint(50, 750), random.randint(50, 550)))
        #     self.screen.blit(self.ice, (200, 200))
        screen.blit(self.image, (self.rect_x, self.rect_y))
