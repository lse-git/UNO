import random

class Uno:
    class Player():
        def __init__(self):
            self.deck = []

    def __init__(self):
        # Create Deck
        self.colgreen = '\033[32m'
        self.colreset = '\033[m'
        self.deck = []
        self.colours = ["b", "g", "r", "y"]
        self.special_cards_without_colour = ["f", "c"]           # f = draw four, c = choose color      (n = none)
        self.special_cards_with_colour = ["t", "v", "s"]         # t = draw two, v = reverse, s = suspend
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
        print("TEMP Deck - Original: {}".format(self.deck))
        print("TEMP Card count - Original: {}".format(len(self.deck)))

        # shuffle deck
        self.shuffle_deck()
        print("TEMP Deck - Shuffle: {}".format(self.deck))
        print("TEMP Card count - Shuffle: {}".format(len(self.deck)))

        # Create Players
        self.player_quantaty = int(input(self.colgreen + "How many players " + self.colreset))          # Asks after player number
        self.players = []
        for self.player in range(self.player_quantaty):
            self.players.append(Uno.Player())                             # Create Players

        # Give each player 7 cards
        for i in self.players:
            self.give_player_card(i, 7)
            print("TEMP Deck - Player {}: {}".format(self.players.index(i),i.deck))
            print("TEMP Card count - Player: {}".format(len(i.deck)))

        # Make opencard list
        self.opendeck = []
        self.opendeck.append(self.deck.pop(0))
        print("TEMP Deck - Open deck: {}".format(self.opendeck))
        print("TEMP Card count - Open deck: {}".format(len(self.opendeck)))

        print("TEMP Deck - Closed deck: {}".format(self.deck))
        print("TEMP Card count - Closed deck: {}".format(len(self.deck)))

        # TEMP counts total number of cards
        cardcount = 0
        for i in self.players:
            cardcount += len(i.deck)
        print("TEMP Total number of cards: {}".format(cardcount + len(self.deck) + len(self.opendeck)))

        # Choose random starting player
        self.start_player_index = random.randint(0, self.player_quantaty - 1)
        print("starting player: " + str(self.start_player_index))        # Choose random player index

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
                card = "n" + special
        return(card)

    def shuffle_deck(self):
        """Shuffles the Deck"""
        random.shuffle(self.deck)
    
    def give_player_card(self, playerobj, num_of_cards=1):
        """Give player in self.players with index playerindex num_of_cards cards from closed deck"""
        for i in range(num_of_cards):
            playerobj.deck.append(self.deck.pop(-1))
    
    def play_card(self, playerobj):
        pc_index = input(self.colgreen + "Deck Player {}, what card between 1 and {} do you want to play? " + self.colreset.format(self.players.index(playerobj), len(playerobj.deck)))
        self.opendeck.append(playerobj.deck.pop(int(pc_index)-1))

    def print_cards(self, playerobj):
        print("TEMP Deck - Open deck: {}".format(self.opendeck))
        print("TEMP Card count - Open deck: {}".format(len(self.opendeck)))

        print("TEMP Deck - Closed deck: {}".format(self.deck))
        print("TEMP Card count - Closed deck: {}".format(len(self.deck)))

        print("TEMP Deck - Player {}: {}".format(self.players.index(playerobj),playerobj.deck))
        print("TEMP Card count - Player: {}".format(len(playerobj.deck)))