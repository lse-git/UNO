from uno import Uno

if __name__ == "__main__":
    game = Uno()
    while True:
        for player in game.players:
            game.give_player_card(player)
            print(player.deck)
            print(len(player.deck))