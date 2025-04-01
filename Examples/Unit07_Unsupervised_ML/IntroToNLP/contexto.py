"""
A basic version of the Contexto 
game that uses word similarity to 
help the user guess the word.

@author: Nandhini Namasivayam
@version: 03/31/2024
"""
from nltk.corpus import wordnet as wn
import random

class Contexto:
    def __init__(self, filename):
        # Load the words from file
        self.words = self.load_words(filename)

        # Pick a word at random
        self.word = random.choice(self.words)
        

        # Get the synonyms for hints
        self.synonyms = self.get_synonyms()

    def load_words(self, filename):
        """
        Loads the words from the provided file

        Args:
            filename (str): Filepath for the words

        Returns:
            list[str]: list of lowercase words
        """
        with open(filename, 'r') as file:
            words = [line.lower().strip() for line in file.readlines()]
        return words
    
    def get_synonyms(self):
        """
        Generates all synonyms for self.word
        based off of WordNet

        Returns:
            list[str]: A list of synonyms for self.word
        """
        synonyms = []
        
        # TODO: Complete this function
        # Loop through all the synsets for the word
        for syn in wn.synsets(self.word):
            # Loop through all lemmas
            for lemma in syn.lemmas():
                if lemma.name() not in synonyms:
                    synonyms.append(lemma.name())
        
        return synonyms

    def get_a_hint(self):
        """
        Prints a hint for the user. The hint is 
        a synonym and that synonym's similarity score
        to the actual word.

        Once the hint is provided, the synonym is 
        removed from the list of synonyms.
        """
        # If there are no synonymsd
        if len(self.synonyms) < 1:
            print("Sorry, you are out of hints")
            return
        

        # TODO: Complete this functihon
        # synonyms = self.get_synonyms()
        synonym = self.synonyms[0]
        self.synonyms.remove(synonym)

        print(synonym + "has a score of " + str(self.calculate_similarity(synonym, self.word)))
            

    
    def calculate_similarity(self, guess, mode=0):
        """
        Calculates and returns the similarity of 
        guess and self.word.

        Args:
            guess (str): The user's guess
            mode (int, optional): How to calculate similarity. Defaults to 0.
             0: Wu-Palmer Similarity 

        Returns:
            float: similarity score
        """
        # TODO: Complete this function

        guess_syn = wn.synsets(guess)[0]
        word_syn = wn.synsets(self.word)[0]
        
        return word_syn.wup_similarity(guess_syn)
    

    def run(self):
        """
        Main game loop. Runs until 
        the user quits or guesses the 
        word correctly
        """

        # Instructions
        print("\nWelcome to Contexto!")

        # Main game loop
        while True:
            guess = input("Guess a word, enter 'h' for a hint, or enter 'q' to reveal the answer: ")

            # TODO: Complete the options
            if guess == "h":
                self.get_a_hint()
            elif guess == "q":
                print(self.word)
            elif self.calculate_similarity(guess) == 1:
                print("You win")
                break
            else:
                print(self.calculate_similarity(guess))

            


if __name__ == "__main__":
    contexto_game = Contexto("data/words.txt")
    contexto_game.run()
