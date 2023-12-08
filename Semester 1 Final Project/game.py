import pygame
import sys
from car import Car
from bot import Bot

class Game:
    # Creating display info
    START_X, START_Y = 24, 24
    SPACING = 50
    BACKGROUND_COLOR = (0, 0, 0)
    WIDTH, HEIGHT = 800, 600

    def __init__(self):

        # Initialize Pygame
        pygame.init()
 
        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Car")

        self.car = Car(self)
        # self.ai_1 = Bot(self)
        # self.ai_2 = Bot(self)
        # self.ai_3 = Bot(self)
        # self.ai_4 = Bot(self)
        # self.ai_5 = Bot(self)
        # self.ai_6 = Bot(self)
        # self.ai_7 = Bot(self)
        # self.ai_8 = Bot(self)

        # enemies = [self.ai_1, self.ai_2, self.ai_3, self.ai_4, self.ai_5, self.ai_6, self.ai_7, self.ai_8]

        # Draw the initial screen
        self.screen.fill(self.BACKGROUND_COLOR)

        
    def run(self):
        # Main game loop
        running = True

        # Draw Initial Screen
        self.screen.fill(self.BACKGROUND_COLOR)
        self.car.draw(self.screen)

        while running:
            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw to the screen
            self.screen.fill(self.BACKGROUND_COLOR)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.velocity_y += 10
                        self.move_up()
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.velocity_y += 10
                        self.move_down()
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.velocity_x
                        self.move_left()
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.velocity_x
                        self.move_right()
            
            pygame.display.flip()


        
        

            
            # elif event.type == pygame.KEYUP:
            #     if (
            #         event.key == pygame.K_UP
            #         or event.key == pygame.K_DOWN
            #         or event.key == pygame.K_LEFT
            #         or event.key == pygame.K_RIGHT
            #     ):
            #         direction = (0, 0)
        # Quit Pygame
        pygame.quit()
        sys.exit()

        
        


if __name__ == "__main__":
    pm = Game()
    pm.run()