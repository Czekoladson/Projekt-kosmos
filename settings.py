import pygame

class Settings():

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (128,128,128)
        self.ship_speed = 0.9
        self.ship_limit = 3
        self.bullet_speed = 0.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 4
        self.alien_width = 50
        self.alien_height = 47
        self.alien_speed = 0.13