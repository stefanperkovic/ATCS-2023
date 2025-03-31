import pygame
from fsm import FSM

class MazeBot(pygame.sprite.Sprite):

    def __init__(self, game, x=50, y=50):
        super().__init__()

        self.game = game

        # Load initial image
        self.image = pygame.image.load("assets/images/bot.png")
        self.rect = self.image.get_rect()

        # Set rectangle
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.centerx = x
        self.rect.centery = y

        # The map of the maze
        self.maze = self.game.txt_grid

        # The route the bot will take to get to the $
        self.path = []

        # TODO: Create the Bot's finite state machine (self.fsm) with initial state
        self.fsm = FSM("SOUTH")
        self.init_fsm()

        
    
    def init_fsm(self):
        # TODO: Add the state transitions
        states = ["SOUTH", "EAST", "NORTH", "WEST", "BSOUTH", "BEAST", "BNORTH", "BWEST"]
        actions = [self.move_south, self.move_east, self.move_north, self.move_west]
        for i in range(len(states)):
            # While in all modes
            self.fsm.add_transition(" ", states[i], actions[i % 4], states[i])
            self.fsm.add_transition("#", states[i], None, states[(i + 1) % 4])
            self.fsm.add_transition("$", states[i], "Gameover")

            # While in normal mode
            if i < 4:
                self.fsm.add_transition("B", states[i], actions[i], states[i + 4])
                self.fsm.add_transition("X", states[i], None, states[(i + 1) % 4])

            # While in breaker mode
            if i >= 4:
                self.fsm.add_transition("B", states[i], actions[i - 4], states[i - 4])
                self.fsm.add_transition("X", states[i], actions[i - 4], states[i])

    
    def get_state(self):
        # TODO: Return the maze bot's current state
        return self.fsm.current_state
        
    
    def move_south(self):
        """
        Changes the bot's location 1 spot South
        and records the movement in self.path
        """
        self.rect.centery += self.game.SPACING
        self.path.append("SOUTH")

    def move_east(self):
        """
        Changes the bot's location 1 spot East
        and records the movement in self.path
        """
        self.rect.centerx += self.game.SPACING
        self.path.append("EAST")

    def move_north(self):
        """
        Changes the bot's location 1 spot North
        and records the movement in self.path
        """
        self.rect.centery -= self.game.SPACING
        self.path.append("NORTH")

    def move_west(self):
        """
        Changes the bot's location 1 spot West
        and records the movement in self.path
        """
        self.rect.centerx -= self.game.SPACING
        self.path.append("WEST")
    
    def get_next_space(self):
        """
        Uses the bot's current state to determine the next 
        space in the maze the bot would go to. The next 
        space is returned as a String from self.maze.

        Ex. If the bot is facing South, you should get 
        the character one row down from you.

        Returns:
            String: The next character in the maze the bot could go to
        """

        # This is the current x and y indices of the bot in the maze
        grid_x = self.rect.centerx // self.game.SPACING
        grid_y = self.rect.centery // self.game.SPACING

        # TODO: Use the bot's current state to determine
        # what the next maze location value is
        if self.get_state() == "SOUTH" or self.get_state() == "BSOUTH":
            grid_x += 1
        elif self.get_state() == "NORTH" or self.get_state() == "BNORTH":
            grid_x -= 1
        elif self.get_state() == "EAST" or self.get_state() == "BEAST":
            grid_y += 1
        elif self.get_state() == "WEST" or self.get_state() == "BWEST":
            grid_y -= 1
        return self.maze[grid_x][grid_y]
    
    def update(self):
        # TODO: Use the finite state machine to process input
        self.fsm.process(self.get_next_space())
        pass
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))
