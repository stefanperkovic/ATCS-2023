"""
A Tic Tac Toe game played on the console with AI player "O"

@author: Ms. Namasivayam
@version: 02/16/2022
"""
import random
import time


class TicTacToe:
    # Class Variables
    NUM_ROWS = 3
    NUM_COLS = 3
    MEDIUM = 4
    HARD = 8

    def __init__(self, player1, player2, difficulty=0):
        # Set player token strings
        self.player1 = player1
        self.player2 = player2

        # Set the difficulty - 0 is easy, 1 is medium, 2 is hard
        # The different difficulties change the AI used
        self.difficulty = difficulty

        # Keep track of whose turn it is
        self.player1_turn = None

        # Set up the board to be empty
        self.board = None
        self.reset_game()

    def reset_game(self):
        """
        Reset the board to be empty
        Set it back to player_1's turn
        """
        self.board = []
        for row in range(self.NUM_ROWS):
            self.board.append(['-', '-', '-'])

        self.player1_turn = True

    def set_difficulty(self, difficulty=0):
        """
        Set the difficulty level to the one provided
        """
        self.difficulty = difficulty

    def print_instructions(self):
        """
        Print the instructions for the game
        """
        print("Welcome to TicTacToe!")
        print("Player 1 is", self.player1, "and Player 2 is", self.player2)
        print("Take turns placing your pieces - the first to 3 in a row wins!")

    def print_board(self):
        """
        Print the board to the console including row and col numbers
        """
        print('\t0\t1\t2')
        for row in range(self.NUM_ROWS):
            print(str(row) + '\t' + '\t'.join(self.board[row]))

    def check_col_win(self, player):
        """
        Determines if the board has a column win for player
        Args:
            player (String): The player to check the win for ("X" or "O")

        Returns:
            int: The column that has the win and -1 otherwise
        """
        for col in range(self.NUM_COLS):
            win = True
            for row in range(self.NUM_ROWS):
                win = win and (self.board[row][col] == player)
            if win:
                return col
        return -1

    def check_row_win(self, player):
        """
        Determines if the board has a row win for player
        Args:
            player (String): The player to check the win for ("X" or "O")

        Returns:
            int: The row that has the win and -1 otherwise
        """
        for row in range(self.NUM_ROWS):
            win = True
            for col in range(self.NUM_COLS):
                win = win and (self.board[row][col] == player)
            if win:
                return row
        return -1

    def check_diag_win(self, player):
        """
        Determines if the board has a diagonal win for player
        Args:
            player (String): The player to check the win for ("X" or "O")

        Returns:
            int: 1 if the win is on the left diagonal, 2 if it is on the right, -1 otherwise
        """
        win_right = True
        win_left = True
        for i in range(self.NUM_ROWS):
            win_right = win_right and (self.board[i][i] == player)
            win_left = win_left and (self.board[i][2-i] == player)

        if win_left:
            return 1
        elif win_right:
            return 2
        else:
            return -1

    def check_win(self, player):
        """
        Determines if the player has a win
        Args:
            player (String): The player to check the win for ("X" or "O")

        Returns:
            boolean: True if player won, False otherwise
        """
        return self.check_col_win(player) != -1 or self.check_row_win(player) != -1 or self.check_diag_win(player) != -1

    def check_tie(self):
        """
        Determines if the board has a tie by checking to see that the board
        is full and neither player has won
        Returns:
            boolean: True for a tie, False otherwise
        """
        players = [self.player1, self.player2]

        # Check that neither player won
        for player in players:
            if self.check_win(player):
                return False

        # Check that the board has no empty spaces
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if self.board[row][col] == '-':
                    return False

        # Otherwise the game is a tie
        return True

    def is_game_over(self):
        """
        Determines if there is a win or tie on the current board
        Returns:
            boolean: True if there is a win or tie, False otherwise
        """
        return self.check_win("X") or self.check_win("O") or self.check_tie()

    def is_valid_move(self, row, col):
        """
        Determines if the provided row and col constitute a valid move
        by checking that it is within bounds and an empty space
        Args:
            row (int): row number indexed at 0
            col (int): col number indexed at 0

        Returns:
            boolean: True if the move is valid and False otherwise
        """
        return (row < self.NUM_ROWS) and (col < self.NUM_COLS) and (self.board[row][col] == '-')

    def place_player(self, player, row, col):
        """
        Places the given player at the row and col
        Args:
            player (String): player token ("X" or "O")
            row (int): row number indexed from 0
            col (int): col number indexed from 0
        """
        self.board[row][col] = player

    def take_manual_turn(self, player):
        """
        Through the console, prompts the user to enter a row
        and col value. If the value is not valid, prompts the user again.
        Places the token at the provided row and col.
        Args:
            player (String): player whose turn it is ("X" or "O")
        """
        valid = False
        while not valid:
            try:
                row = int(input("Enter a row: "))
                col = int(input("Enter a column: "))
                valid = self.is_valid_move(row, col)
                if not valid:
                    print("Please enter a valid move.")
                else:
                    self.place_player(player, row, col)
            except ValueError:
                print("Please enter a valid move.")

    def take_random_turn(self, player):
        """
        Randomly selects a row and column and 
        places the player there
        Args:
            player (String): player token ("X" or "O")
        """
        rows = []
        cols = []
        for row in range(3):
            for col in range(3):
                if self.is_valid_move(row, col):
                    rows.append(row)
                    cols.append(col)
        index = random.randrange(0, len(rows) - 1)
        self.place_player(player, rows[index], cols[index])
        pass

    def take_turn(self, player):
        """
        Calls a manual turn for player 1
        Determines the AIs turn depending on the difficulty
        Args:
            player (String): The player ("X" or "O")
        """
        print(player+"'s Turn")
        if player == "X":
            self.take_manual_turn(player)
        else:
            self.take_minimax_turn(player)

    def play_game(self):
        """
        Continuously take turns until the game is over
        """
        self.print_instructions()
        self.print_board()

        while True:
            player = self.player1 if self.player1_turn else self.player2
            self.take_turn(player)
            self.print_board()
            if self.check_win(player):
                print(player + " wins!")
                break
            elif self.check_tie():
                print("It's a Tie!")
                break
            else:
                self.player1_turn = not self.player1_turn

    def minimax(self, depth, player="O"):
        # Switches players every turn
        next_player = "O" if player=="X" else "X"

        
        if self.check_win("O") == True:
            return (1, None, None)
        elif self.check_win("X") == True:
            return (-1, None, None)
        elif self.check_tie() == True:
            return (0, None, None)
        if depth <= 0:
            return (0, None, None)
        
        if player == "O":
            max_score = -2
            best_row = 0
            best_col = 0
            for row in range(self.NUM_ROWS):
                for col in range(self.NUM_COLS):
                    if self.board[row][col] == "-":
                        self.place_player(player, row, col)
                        score_tuple = self.minimax(depth - 1, next_player)
                        self.place_player("-", row, col)
                        if score_tuple[0] > max_score:
                            max_score = score_tuple[0]
                            best_row = row
                            best_col = col
            return (max_score, best_row, best_col)
        
        elif player == "X":
            worst_row = 0
            worst_col = 0
            min_score = 2
            for row in range(self.NUM_ROWS):
                for col in range(self.NUM_COLS):
                    if self.board[row][col] == "-":
                        self.place_player(player, row, col)
                        score_tuple = self.minimax(depth - 1, next_player)
                        self.place_player("-", row, col)
                        if score_tuple[0] < min_score:
                            min_score = score_tuple[0]
                            worst_row = row
                            worst_col = col
            return (min_score, worst_row, worst_col)
            
    def take_minimax_turn(self, player):
        depth = 2
        score, row, col = self.minimax(depth, player)
        self.place_player(player, row, col)

        

if __name__ == "__main__":
    game = TicTacToe("X", "O")
    game.play_game()
