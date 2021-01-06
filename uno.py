import random:

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
