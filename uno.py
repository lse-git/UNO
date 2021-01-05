import random

class Uno:
    class Player():
        def __init__(self):
            self.deck = []

    def __init__(self):
        # Create Deck
        self.deck = []
        self.colours = ["b", "g", "r", "y"]
        self.special_cards_with_colour = ["+2", "rt", "sp"]         # +2 = draw 2, rt = retour, sp = suspend
        self.special_cards_without_colour = ["+4", "chc"]           # +4 = draw 4, chc = choose color
        # add normal cards
        for i in range(0, 10):
            for self.colour in self.colours:
                if i == 0:
                    self.deck.append(self.create_card(i, self.colour))
                elif i in range(1, 10):
                    for j in range(2):
                        self.deck.append(self.create_card(i, self.colour))
        # add special cards
        for self.card_types in self.special_cards_without_colour:
            for i in range(4):
                self.deck.append(self.create_card(special=self.card_types))
        for self.card_types in self.special_cards_with_colour:
            for self.colour in self.colours:
                for i in range(2):
                    self.deck.append(self.create_card(col=self.colour, special=self.card_types))
        # shuffle deck
        self.shuffle_deck()

        # Create Players
        self.player_quantaty = int(input("How many players "))          # Asks after player number
        self.players = []
        for self.player in range(self.player_quantaty):
            self.players.append(Uno.Player())                             # Create Players
        
        # Give each player 7 cards
        for i in range(len(self.players)):
            self.give_player_card(playerindex=i, num_of_cards=7)

    def create_card(self, num=None, col=None, special=None):
        """Returns new Card (as string)

        - number int(num) + colour str(col)
        - colour str(col) + special card str(special)
        - special card str(special)"""
        if special == None:
            card = str(num) + col
        else:
            if col != None and special != None:
                card = col + special
            else:
                card = special
        return(card)

    def shuffle_deck(self):
        """Shuffles the Deck"""
        random.shuffle(self.deck)
    
    def give_player_card(self, playerindex, num_of_cards=1):
        """Give player in self.players with index playerindex num_of_cards cards from closed deck"""
        for i in range(num_of_cards):
            self.players[playerindex].deck.append(self.deck.pop(-1))