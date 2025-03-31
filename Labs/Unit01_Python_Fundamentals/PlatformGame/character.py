import pygame

class Character:
    # Written by OpenAi Chatgpt
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.jump_power = 10
        self.is_jumping = False
        self.jump_count = 0
        self.health = 100

    # Written by OpenAi Chatgpt
    def move_left(self):
        self.rect.x -= self.speed

    # Written by OpenAi Chatgpt
    def move_right(self):
        self.rect.x += self.speed

    # Written by OpenAi Chatgpt
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 0

    # Written by Stefan Perkovic and Joshua Benyo Baker
    def die(self):
        self.rect.x = 690
        
    # Written by OpenAi Chatgpt
    def apply_gravity(self):
        if not self.is_jumping:
            if self.rect.y < 400:
                self.rect.y += 10

    # Written by OpenAi Chatgpt 
    def update(self):
        if self.is_jumping:
            if self.jump_count < self.jump_power:
                self.rect.y -= 3
                self.jump_count += 1
            else:
                self.is_jumping = False
                self.jump_count = 0
        else:
            self.apply_gravity()

    # Written by OpenAi Chatgpt
    def draw(self, screen):
        screen.blit(self.image, self.rect)
