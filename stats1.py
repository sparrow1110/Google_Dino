import platform
import os
import database

# Информация о игроке и игре.
class Stats:
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        self.paus = False
        if platform.system() == 'Windows':
            self.name = os.getlogin()
        else:
            self.name = os.environ.get('LOGNAME')
        self.high_score = database.load_high_score(self.name)

    def reset_stats(self):
        # Статистика изменяющаяся во время игры.
        self.score = 0
