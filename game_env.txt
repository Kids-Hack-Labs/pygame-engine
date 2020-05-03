import pygame, sys

from gameobject_example import GameObject

pygame.init()

# 16:9 aspect ratio
screen_size = (800, 450)
screen = pygame.display.set_mode(screen_size)

screen.fill((255, 255, 255))

def gameLoop():

    # create the gameobject instance
    myObject = GameObject(200, 200)

    # challenge q: what happens when you create more than one GameObject?

    isRunning = True
    while isRunning:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('closing...')
                isRunning = False
                pygame.quit()
                sys.exit() # add

        # erase everything on the screen
        # so we can draw everything in its new position
        screen.fill((255, 255, 255))

        # call our update method
        # this method is responsible for movement
        myObject.update()

        # draw our gameobject to the screen
        myObject.render(screen)
        
        pygame.display.flip()

if __name__ == '__main__':
    gameLoop()
