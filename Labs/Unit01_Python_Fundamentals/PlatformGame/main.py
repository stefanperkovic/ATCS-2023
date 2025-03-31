import pygame
import time
from character import Character



class Game:
    # Written by OpenAi ChatGpt 
    def __init__(self, title, width, height):
        pygame.init()

        # Constants
        self.WIDTH = width
        self.HEIGHT = height
        self.WHITE = (255, 255, 255)

        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(title)

      # Load the background image
        self.background = pygame.image.load("background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.game_over = pygame.image.load("gameover.jpg")
        self.game_over = pygame.transform.scale(self.game_over, (self.WIDTH, self.HEIGHT))

        # Initialize game objects and variables here
        self.character = Character("jedi.png", 50, self.HEIGHT - 200)
        # Add other game objects and variables as needed
        self.droid = Character("enemy.png", 690, self.HEIGHT - 225)




    def run(self):
        # Written by Stefan Perkovic and Joshua Benyo Baker
        self.screen.blit(self.background, (0, 0))
        self.character.draw(self.screen)
        self.droid.draw(self.screen)
        # Written by OpenAi ChatGpt 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Handle user input and update game logic here
            keys = pygame.key.get_pressed()

            # Written by Stefan Perkovic and Joshua Benyo Baker
            self.droid.move_left()

            if keys[pygame.K_SPACE]:
                self.character.jump()

            # Written by Stefan Perkovic and Joshua Benyo Baker
            if self.character.rect.x + 50 > self.droid.rect.x: 
                if self.character.rect.y + 50 > self.droid.rect.y:
                    self.background = self.game_over
                    self.screen.blit(self.background, (0, 0))
                    
            
                else:
                    self.droid.die()
                    self.droid.speed += 1
               
                
                
            # Written by OpenAi Chatgpt
            self.character.update()
            # Update other game objects and logic here

            # Redraw the background
            self.screen.blit(self.background, (0, 0))

            # Draw game objects here
            self.character.draw(self.screen)
            self.droid.draw(self.screen)
            # Draw other game objects here

            # Update the display
            pygame.display.update()

        # Quit the game
        pygame.quit()
# Written by OpenAi Chatgpt
if __name__ == "__main__":
    game = Game("My Game", 800, 600)
    game.run()
