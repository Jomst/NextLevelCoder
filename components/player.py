import pygame

from utils.constants import (
    WHITE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH
)

from components.bullet import Bullet

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((50,50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT - 10

    def update(self):
        self.movement_on_x = 10
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.movement_on_x
        elif key[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.movement_on_x

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets = pygame.sprite.Group()
        self.bullets.add(bullet)
