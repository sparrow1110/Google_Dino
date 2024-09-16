import random

import database
from pygame.sprite import Sprite

# Загрузка картинок.
imgPter = database.load_images('pter1', 'pter2')
imgCactus = database.load_images('cactus1', 'cactus2')

# Класс, описывающий объекты препятствий.
class Cactus(Sprite):
    speed = 0.9*7

    def __init__(self, screen):
        super(Cactus, self).__init__()
        self.screen = screen
        self.frame = 0
        k = random.randint(0, 4)

        self.screen_rect = screen.get_rect()
        if k == 0:
            self.image = [imgCactus[self.frame]]
            self.rect = self.image[self.frame].get_rect()
            self.rect.bottom = self.screen_rect.bottom - 131
        elif k == 1:
            self.image = imgPter
            self.rect = self.image[self.frame].get_rect()
            self.rect.bottom = self.screen_rect.bottom - 160
        else:
            self.image = [imgCactus[1]]
            self.rect = self.image[self.frame].get_rect()
            self.rect.bottom = self.screen_rect.bottom - 131

        self.rect.centerx = self.screen_rect.right
        self.center = float(self.rect.centerx)

    def update(self):
        self.center -= Cactus.speed
        self.rect.centerx = self.center
        self.frame = (self.frame + 0.02 * 10) % len(self.image)
        self.speed += 0.01*10

    def draw(self):
        self.screen.blit(self.image[int(self.frame)], self.rect)

