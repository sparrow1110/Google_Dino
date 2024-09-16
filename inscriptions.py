import pygame.font
import database

# Загрузка изображений кнопок.
imgButtons = database.load_images('restart', 'pause', 'play')

# Надписи и кнопки.
class Inscriptions:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 100)
        self.death_text()
        self.pause()

    def death_text(self):
        self.text_img = self.font.render("Game Over", True, self.text_color, (255, 255, 255))
        self.text_rect = self.text_img.get_rect()
        self.image = imgButtons[0]
        self.image_rect = self.image.get_rect()

        self.text_rect.centerx = self.screen_rect.centerx
        self.text_rect.top = self.screen_rect.top + 250
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.top = self.screen_rect.top + 320

    def pause(self):
        self.button = imgButtons[1]
        self.button_rect = self.button.get_rect()
        self.button_rect.centerx = self.screen_rect.centerx
        self.button_rect.top = 10

    def play(self):
        self.button = imgButtons[2]
        self.button_rect = self.button.get_rect()
        self.button_rect.centerx = self.screen_rect.centerx
        self.button_rect.top = 10

    def show_death_text(self):
        self.screen.blit(self.text_img, self.text_rect)
        self.screen.blit(self.image, self.image_rect)

    def show_button(self):
        self.screen.blit(self.button, self.button_rect)