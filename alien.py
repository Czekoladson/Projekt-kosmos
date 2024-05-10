import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.height
        self.rect.y = self.rect.width

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_speed
        self.rect.y = self.y
