# main file for defining our ship object
# importing req.
import pygame

# make a class ship
class Ship():
#     basic method
# need argument screen to load image upon
# need game settings(gs) as arguments
    def __init__(self,screen,gs):
        # loading the image as png so no background
        self.image = pygame.image.load('ship.png')
        # loading screen
        self.screen = screen
        # loading gs
        self.gs = gs
        # making image as rectangle
        self.rect = self.image.get_rect()
        # making screen as a rctangle
        self.screen_rect = self.screen.get_rect()
        # aligning center of image to center of screen
        self.rect.centerx = self.screen_rect.centerx
        # aligning bottom of image to bottom of screen
        self.rect.bottom = self.screen_rect.bottom
#         making center as float
        self.centerx = float(self.rect.centerx)


#         Defining the movement - Flag as False
        self.move_right = False
        self.move_left = False
    #     updating the position of ship on altering FLAG
    def update(self):
#         if true move
# move within ranges
        if self.move_right and self.rect.right < self.screen_rect.right:
#             move right
            self.rect.centerx += self.gs.ship_speed
        if self.move_left and self.rect.left > 0:
# move lft
            self.rect.centerx -= self.gs.ship_speed




    # defining blitme function to blit ship on screen
    def blitme(self):
#             need to blit on screen
# need to blit image and rect with that too
        self.screen.blit(self.image,self.rect)

