import pygame

class Settings():

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (128,128,128)
        self.ship_speed = 0.9
        self.bullet_speed = 0.7
        self.alien_speed = 0.13
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 4
        self.alien_width = 50
        self.alien_height = 47
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.points_for_alien_shot = 50
        self.ship_number = 3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed = 0.10
        self.points_for_alien_shot = int(self.points_for_alien_shot * self.score_scale)

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        print(self.points_for_alien_shot)
