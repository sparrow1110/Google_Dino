import pygame.font

# Вывод игровой информации.
class Scores:
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()

    def image_score(self):
        self.score_img = self.font.render("Счет: " + str(int(self.stats.score)), True, self.text_color, (255, 255, 255))
        self.score_rect = self.score_img.get_rect()

        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score_image = self.font.render("Рекорд: " + str(int(self.stats.high_score)), True, self.text_color, (255, 255, 255))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.left + 85
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
