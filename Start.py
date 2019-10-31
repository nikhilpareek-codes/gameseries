import pygame
import sys
# import Settings
from game_settings import Settings
# import game functions
import game_functions as gf
# importing ship class
from ship import Ship
# we need Group to store bullets
from pygame.sprite import Group



def start():
    # initiating pygame
    pygame.init()
    # making instance for game settings
    gs = Settings()
    # passing argument defined as sequence of tuple
    screen = pygame.display.set_mode(gs.size)
    # passing caption for top of GUI
    pygame.display.set_caption(gs.caption)


    # making instance of ship
    ship = Ship(screen,gs)

    # Making instance of bullet
    bullets = Group()

    # Initiating main loop for  continuous update
    while True:
    #     for cehecking key/mouse inputs
    # calling function from game_function module
        gf.chk_events(gs,screen,ship,bullets)
    # updating the bullets
        bullets.update()
    # Updating the screen
        gf.update(gs,screen,ship,bullets)


# Start the game
start()



