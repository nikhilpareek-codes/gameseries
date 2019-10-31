import pygame
import sys
# importing bullet
from bullet import Bullet
# check key down events
def chk_keydown_events(event,gs,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
#         create new bullet
        new_bullet = Bullet(gs,screen,ship)
        bullets.add(new_bullet)

# Check key up events
def chk_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False


# Defining the function for checking events
# depends on ship to change flag value
def chk_events(gs,screen,ship,bullets):
    # loop for continuous check of events
    for event in pygame.event.get():
        # check for event type
        if event.type == pygame.QUIT:
            # Defining the response
            sys.exit()
        #     if there's a key press
        elif event.type == pygame.KEYDOWN:
#             checking which key is pressed
            chk_keydown_events(event,gs,screen,ship,bullets)
# to stop ship we need to make value false as KeyUP
        elif event.type == pygame.KEYUP:
#             checking which key is released
            chk_keyup_events(event,ship)




# defining the function for upadating changes on screen
# update depen upon gs for bg_color
# bg_color needs screen too
# need ship to update ship on image
def update(gs,screen,ship,bullets):
    # screen color
    screen.fill(gs.bgcolor)
    # updating position of ship
    ship.update()
    # Redraw bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # drawing the ship
    ship.blitme()
    # update all the changes made on the screen
    pygame.display.flip()
