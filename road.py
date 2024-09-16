import pygame
import database

# Класс, описывающий дорогу.
class Road(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Road, self).__init__()
        self.screen = screen
        self.image = database.load_images('road')[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 100

    def output(self):
        self.screen.blit(self.image, self.rect)
