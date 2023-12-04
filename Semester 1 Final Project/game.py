import pygame


class Game:
    # Creating display info
    START_X, START_Y = 24, 24
    SPACING = 50
    BACKGROUND_COLOR = (0, 0, 0)
    WIDTH, HEIGHT = 800, 600

    def __init__(self):
        # Draw the initial screen
        self.screen.fill(self.BACKGROUND_COLOR)
 
        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Car")

        
        


    def run(self):
        # Main game loop
        running = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = (0, -speed)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = (0, speed)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = (-speed, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = (speed, 0)
            elif event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_UP
                    or event.key == pygame.K_DOWN
                    or event.key == pygame.K_LEFT
                    or event.key == pygame.K_RIGHT
                ):
                    direction = (0, 0)
        
        


if __name__ == "__main__":
    pm = MangoGame()
    pm.run()