'''
    Main App file
    Simply instantiates the Game class and runs it
    with the config parameters specified in
    "window_size" and "title"
'''
from engine.game import Game

def main():
    window_size = (800, 450)
    title = "Game"
    g = Game(window_size, title)

    # KNOWN BUG: window doesn't close on exit
    g.run()

if __name__ == "__main__":
    main()
