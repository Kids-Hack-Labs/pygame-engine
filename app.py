'''
    Main App file
    Simply instantiates the Game class and runs it
    with the config parameters specified in
    "window_size" and "title"
'''
from engine.game_env import Game

def main():
    window_size = (1024, 768)
    title = "Game"
    g = Game(window_size, title)
    g.run()

if __name__ == "__main__":
    main()
