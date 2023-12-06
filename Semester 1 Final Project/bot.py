import pygame



class Bot:
    WIDTH = 50
    HEIGHT = 50

    def __init__(self):
        self.truck = pygame.image.load("truck.png")
        self.truck = pygame.transform.scale(self.truck, (self.WIDTH, self.HEIGHT))
        

        # Initialize Pygame 
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.ghost_timer = 8000


        def run(self):
        # Main game loop
        running = True

        # Draw the initial screen
        self.screen.fill(self.BACKGROUND_COLOR)
        self.blocks.draw(self.screen)
        self.mango.draw(self.screen)
        
        while running:
            # Set fps to 120
            self.dt += self.clock.tick(120)

            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Only update every 120 fps
            if self.dt > 120:
                self.dt = 0
                self.mango.update()

                # Draw to the screen
                self.screen.fill(self.BACKGROUND_COLOR)
                self.blocks.draw(self.screen)
                self.mango.draw(self.screen)

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()
    