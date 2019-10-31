# Module to define our ship object
import pygame
from pygame.sprite import Sprite

# class bullet be a sub class of Sprite
# using inheritance
class Bullet(Sprite):
    def __init__(self,gs,screen,ship):
        # initialization of bullet
        super(Bullet,self).__init__()
        self.screen = screen
#         creating a bullet at 0,0
        self.rect = pygame.Rect(0,0,gs.bullet_width
                                , gs.bullet_height)
        # aligning center of bullet to ship
        self.rect.centerx = ship.rect.centerx
#        aligning top of bullet with top of ship
        self.rect.top = ship.rect.top

#         bullet position as decimal value
        self.y = float(self.rect.y)

#         color of bullet
        self.color = gs.bullet_color
        # speed of bullet
        self.speed = gs.bullet_speed

# updating the position of bullets
    def update(self):
#         move bullet upwards
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


