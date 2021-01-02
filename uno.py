from tkinter import *
import random
import time

decknumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deckcolors = ['red', 'green', 'blue', 'yellow']
deck = []
player1cards = []

def create_deck():
    '''Creates UNO Deck and returns it shuffeled as 'randomdeck'

    Deck contains:
        3x every color/number combination
            (red, yellow, green, blue) + (1, 2, 3, 4, 5, 6, 7, 8, 9)
        2x every color/+2 combination'''
    global randomdeck
    for i in range(3):
        for j in range(0, len(deckcolors)):
            y = deckcolors[j]
            for k in range(0, len(decknumbers)):
                x = decknumbers[k]
                deck.append([x, y])
    for l in range(2):
        for m in range(0, len(deckcolors)):
            y = deckcolors[m]
            deck.append(['+2', y])
    randomdeck = random.sample(deck, len(deck))

def printcard(x, y, size, player, deckindex):
    '''Prints given Card at given Position in given Size

    Arguments:
        x   =   middle x position in pixels
        y   =   middle y position in pixels
        size    =   half of the width of the card
        player  =   from whitch list the card should be used
            (0 = opendeck,
            1 = player1,
            2 = player2)
        deckindex   =   which index of given list should be used

        height of card is 1.5 times the width of the card'''
    if player == 1:
        card = c.create_rectangle(x - size, y - size * 1.5, x + size, y + size * 1.5, fill=player1[deckindex][1])
        num = c.create_text(x, y, text=player1[deckindex][0], font=('Helvetica', int(size / 2)))
        player1cards.append([card, num])
    if player == 0:
        card = c.create_rectangle(x - size, y - size * 1.5, x + size, y + size * 1.5, fill=opendeck[deckindex][1])
        num = c.create_text(x, y, text=opendeck[deckindex][0], font=('Helvetica', int(size / 2)))

def printcardback(x, y, size):
    '''Prints the back of a Card'''
    cardback = c.create_rectangle(x - size, y - size * 1.5, x + size, y + size * 1.5, fill='black')
    cardbackoval = c.create_oval(x - size, y - size * 1.5, x + size, y + size * 1.5, fill='grey')
    cardbacktext = c.create_text(x, y, text='UNO', font=('Helvetica', int(size / 2)), fill='black')

create_deck()
player1 = randomdeck[0: 5]
opendeck = randomdeck[0]
del randomdeck[0: 6]
print('deck:')
print(randomdeck)
print('player1 deck:')
print(player1)

window = Tk()
window.title('UNO')

c = Canvas(window, width=1500, height=800)
c.pack()

printcardback(200, 400, 100)
opencard = printcard(500, 400, 100, 0, 0)
for i in range(len(player1)):
    printcard(100 * (i + 1), 700, 40, 1, i)
    time.sleep(0.25)
    window.update()

def click(*args):
    opendeck.append(player1[0])
    del player1[0]
    c.delete(player1cards[0])
    c.delete(opendeck[0])
    printcard(500, 400, 100, 0, 0)

c.tag_bind(player1cards[0][0], '<Button-1>', click)

window.mainloop()