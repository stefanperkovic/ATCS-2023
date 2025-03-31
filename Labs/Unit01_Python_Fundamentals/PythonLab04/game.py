"""
A game of Crazy 8s

ATCS 2023-2024
"""

# TODO 1: Import Statements
from card import Card
from deck import Deck
from player import Player


class Game:
    def __init__(self, player_names):
        self.players = [Player(player) for player in player_names]
        self.deck = Deck()
        self.deck.shuffle()
        self.current_player_index = 0
        self.is_game_over = False

        # Select an initial card
        self.current_card = self.deck.deal()

        self.deal_initial_hand()
    
    def deal_initial_hand(self):
        # TODO 3: Deal 5 cards to each player
        for player in self.players:
            for i in range(5):
                player.draw(self.deck.deal())

    
    def is_valid_card(self, card):
        # TODO 4: Determine if the player's chosen card is valid
        if self.current_card.suit == card.suit:
            return True
        elif self.current_card.rank == card.rank:
            return True
        return False
        

    """
    Determines if the game is over by checking
    if the current player has any cards left
    """
    def check_game_over(self):
        if not self.players[self.current_player_index].has_cards():
            self.is_game_over = True
            print(self.players[self.current_player_index], "wins!")
    
    """
    Draws a card from the deck
    and adds it to the current player's hand
    then displays the new card to the player
    """
    def draw_card(self):
        card = self.deck.deal()
        if card is not None:
            self.players[self.current_player_index].draw(card)
            print("You've drawn", card)

    def play(self):
        while(not self.is_game_over):
            
            # TODO 5: Complete the play function
            for player in self.players:
                print(self.players[self.current_player_index], "'s turn")
                print("The top card is", self.current_card)
                player.show_hand()
                x = int(input("Select the card you would like to play or -1 to pass:"))
                if self.is_valid_card(player.play(x)):
                    self.currentcard = player.play(x)
                else:
                    player.draw(self.deck.deal())
                self.current_player_index += 1
            
                # elif x < len(player.hand):
                #     if player.hand[x].suit == self.current_card.suit and player.hand[x].rank == self.current_card.rank:
                #         self.currentcard = player.play(x)
                #         break
                #     if player.hand[x].rank == 8:
                #         self.currentcard = player.play(x)
                #         break
                #     else:
                #         player.draw(self.deck.deal)  
            



if __name__ == "__main__":
    # TODO 6: Initialize and play the game
    players = ["Joshua", "Stefan", "Elijah"]
    g = Game(players)
    g.play()
    
