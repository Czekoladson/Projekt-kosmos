import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from game_stats import Stats
from start_button import Button

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Inwazja Kosmitów')
        self.stats = Stats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_fleet()
        self.create_button = Button(self,self.screen,"Gra")

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()
            self.ship.update()
            self.update_bullets()
            self.update_aliens()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_play_button(self,mouse_pos):
        button_clicked = self.create_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            if self.create_button.rect.collidepoint(mouse_pos):
                self.stats.reset_stats()
                self.stats.game_active = True

            self.aliens.empty()
            self.bullets.empty()

            self.create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
        elif event.key == pygame.K_g:
            self.stats.game_active
            self.stats.reset_stats()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()

            self.create_fleet()
            self.ship.center_ship()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def fire_bullets(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collision()

    def update_aliens(self):
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship_hit()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print(f'Statek został zestrzelony!!!')
        self.check_aliens_bottom()
    def check_bullet_alien_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True) # False, True jak ma być super pocisk
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()  # cóś nie działa
    def create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number= None):  # Do zmiany none
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self.create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            sys.exit() #do zmiany

    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.ship_blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.create_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


