# module to define settings for our file
# making a class Setting to store all the settings
class Settings():
    # Settings for screen
    def __init__(self):
        self.size = (600,600)
        self.caption = "Alien Hunter"
        self.bgcolor = (230,230,230)

# Ship Speed
        self.ship_speed = 1.5

# Settings for bullets
        self.bullet_speed = 1
        self.bullet_width  = 3
        self.bullet_height = 15
        self.bullet_color = 40,50,60
