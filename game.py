from uno import Uno

if __name__ == "__main__":
    game = Uno()
    while True:
        for player in game.players:
            # give each player one card from deck
            game.give_player_card(player)
            game.print_cards(player)

            # let player choose which card to play
            game.play_card(player)
            game.print_cards(player)