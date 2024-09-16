import pygame.font
import pygame
import sys
from cactus import Cactus
import time
import random
import database

times = time.time()
interval = random.uniform(1, 5)
raz = 0


def events(screen, dino, cacti, stats):
    global times, interval, raz
    # Генерация препятствий.
    if time.time() > times + interval and stats.paus == False:
        new_cactus = Cactus(screen)
        cacti.add(new_cactus)
        times = time.time()
        interval = random.uniform(1.3, 2)

    # Обработка действий игрока.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 2
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 312 < x < 388 and 320 < y < 385:
                return 1
            if 312 < x < 388 and 10 < y < 75:
                if not stats.paus:
                    stats.paus = True
                    raz = time.time() - times
                else:
                    stats.paus = False
                    times = time.time() - raz

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino.mup and not dino.mdown:
                dino.mup = True
                dino.v = 1.5 * 9
            else:
                if event.key == pygame.K_SPACE and dino.mup and not dino.mup2:
                    dino.mup2 = True
                    dino.doub = dino.screen_rect.bottom - 172 - dino.y
                    dino.v = 1.5 * 9
    return 0

# Обновление экрана.
def update(screen, bg_color, road, dino, cacti, sc, inscr, stats):
    screen.fill(bg_color)
    for cactus in cacti.sprites():
        cactus.draw()
    sc.show_score()
    road.output()
    dino.output()
    if stats.paus:
        inscr.play()
        inscr.show_button()
        pygame.display.flip()
        while True:
            events(screen, dino, cacti, stats)
            if not stats.paus:
                inscr.pause()
                break
    if not stats.run_game:
        inscr.show_death_text()
        pygame.display.flip()
        while True:
            k = events(screen, dino, cacti, stats)
            if k == 1:
                check_high_score(stats, sc)
                break
            elif k == 2:
                check_high_score(stats, sc)
                sys.exit()
    inscr.show_button()
    pygame.display.flip()


def update_cactus(cacti):
    cacti.update()
    for cactus in cacti.copy():
        if cactus.rect.centerx < 0:
            cacti.remove(cactus)


def collision(dino, cacti, stats, sc):
    for cactus in cacti.copy():
        if dino.rect.collidepoint(cactus.rect.center[0] - 2, cactus.rect.top + 7) or \
                dino.rect.collidepoint(cactus.rect.center[0], cactus.rect.bottom) or \
                dino.rect.collidepoint(cactus.rect.left + 5, cactus.rect.center[1]) or \
                dino.rect.collidepoint(cactus.rect.right - 4, cactus.rect.center[1] + 2):
            stats.run_game = False
            return 0

    stats.score += 0.1
    sc.image_score()
    sc.image_high_score()

# Проверка нового рекорда.
def check_high_score(stats, sc):
    if stats.score >= stats.high_score:
        stats.high_score = int(stats.score)
        sc.image_high_score()
        database.update_high_score(int(stats.score), stats.name)

