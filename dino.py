from pygame.sprite import Sprite
import database

# Загрузка изображений динозавра.
imgDino = database.load_images('dino1', 'dino2')

# Класс, описывающий динозавра.
class Dino(Sprite):
    def __init__(self, screen):
        super(Dino, self).__init__()
        self.screen = screen
        self.frame = 0
        self.image = imgDino[int(self.frame)]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 200
        self.rect.y = self.screen_rect.bottom - 172
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.mup = False
        self.mdown = False
        self.mup2 = False
        self.doub = 0
        self.v = 0

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_dino(self):
        if self.mup:
            if self.rect.y <= self.screen_rect.bottom - 292 - self.doub:
                self.mup = False
                self.mup2 = False
                self.mdown = True

            else:
                self.y = (self.y - self.v)
                self.rect.y = self.y
                self.v = (self.v - 0.0092*85)
        elif self.mdown:
            if self.rect.y >= self.screen_rect.bottom - 172:
                self.y = self.screen_rect.bottom - 172
                self.rect.y = self.y
                self.mdown = False
                self.doub = 0
            else:
                self.y = (self.y + self.v)
                self.rect.y = self.y
                self.v = (self.v + 0.0092 * 85)
        self.frame = (self.frame + 0.02 * 10) % len(imgDino)
        self.image = imgDino[int(self.frame)]

