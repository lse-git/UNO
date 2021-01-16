from uno import Uno

if __name__ == "__main__":
    game = Uno()
    while True:
        for player in range(len(game.players)):
            print(player)
            input()