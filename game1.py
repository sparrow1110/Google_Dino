import pygame
import control1
from road import Road
from dino import Dino
from pygame.sprite import Group
from stats1 import Stats
from scores1 import Scores
from inscriptions import Inscriptions


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Гугл Динозаврик")  # название
    bg_color = (255, 255, 255)  # цвет фона
    road = Road(screen)
    dino = Dino(screen)
    cacti = Group()
    stats = Stats()
    sc = Scores(screen, stats)
    inscr = Inscriptions(screen)
    FPS = 70
    while True:
        if not stats.run_game:
            break
        control1.events(screen, dino, cacti, stats)
        dino.update_dino()
        control1.update_cactus(cacti)
        control1.collision(dino, cacti, stats, sc)
        control1.update(screen, bg_color, road, dino, cacti, sc, inscr, stats)
        pygame.time.Clock().tick(FPS)


while True:
    run()
