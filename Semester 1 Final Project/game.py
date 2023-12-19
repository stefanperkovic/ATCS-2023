import pygame
import sys
from car import Car
from bot import Bot
from fsm import FSM
from obstacle import Obstacle
"""
    This file implements the game
    Takes in user input to move the car
    Organizes the movement and drawing of bots
    Uses the Finite State Machine to put the car in different
    states if it collides with an obstacle
    Stefan Perkovic December 18 2023
"""
class Game:
    # Creating display info
    START_X, START_Y = 24, 24
    WIDTH, HEIGHT = 800, 600

    def __init__(self):
        # Initialize Pygame
        pygame.init()
 
        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Car")

        # Create User Car
        self.car = Car()

        # Creates the obstacles
        self.ice = Obstacle("ICE")
        self.oil = Obstacle("OIL")

        # Initialize the FSM
        self.fsm = FSM("NORMAL")
        self.init_fsm()

        # Initialize bots
        self.ai_1 = Bot("TRUCK")
        self.ai_2 = Bot("TRUCK")
        self.ai_3 = Bot("TRUCK")
        self.ai_4 = Bot("CAR")
        self.ai_5 = Bot("CAR")
        self.ai_6 = Bot("CAR")
        self.enemies = [self.ai_1, self.ai_2, self.ai_3, self.ai_4, self.ai_5, self.ai_6]

        # Initialiae Background Image
        self.road = pygame.image.load("resources/road.jpg")
        self.road = pygame.transform.scale(self.road, (self.WIDTH, self.HEIGHT))

    def init_fsm(self):
        # Add State Transitions
        self.fsm.add_transition("OIL", "NORMAL", self.car.slow_down, "SLOW")
        self.fsm.add_transition("OIL", "SLOW", self.car.slow_down, "SLOW")
        self.fsm.add_transition("OIL", "BOOST", self.car.slow_down, "SLOW")

        self.fsm.add_transition("ICE", "NORMAL", self.car.speed_up, "BOOST")
        self.fsm.add_transition("ICE", "SLOW", self.car.speed_up, "BOOST")
        self.fsm.add_transition("ICE", "BOOST", self.car.speed_up, "BOOST")

    # Draws the game UI
    def draw_screen(self):
        # Draw Background and Car
        self.screen.blit(self.road, (0,0))
        self.car.draw(self.screen)

        # Draw bots
        for ai in self.enemies:
            ai.draw(self.screen)

        # Draws obstacles
        self.ice.draw(self.screen)
        self.oil.draw(self.screen)

    # Cheks if the user collides with another object
    def check_collision(self):
        # Checks if user collides with another car
        for ai in self.enemies:
            if self.car.pixel_perfect_collision(self.car, ai):
                pygame.quit()
                sys.exit()
        # Checks if user colides with ice or oil and if so calls the fsm
        if self.car.pixel_perfect_collision(self.car, self.ice):
            self.fsm.process("ICE")
        if self.car.pixel_perfect_collision(self.car, self.oil):
            self.fsm.process("OIL")
        
    def run(self):
        # Main game loop
        running = True

        # Draws inital screen
        self.draw_screen()

        # The main loop of the game that only ends when a collision occurs  
        while running:
            # Handle closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draws the screen
            self.draw_screen()

            # Bot Movement
            for ai in self.enemies:
                ai.move_forward()

            # Handles user imput
            self.car.handle_input()

            # Checks collison
            self.check_collision()

            pygame.display.flip()         
        
        # Quit Pygame
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pm = Game()
    pm.run()