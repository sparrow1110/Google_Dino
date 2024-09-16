import sqlite3 as sq
import pygame
import tempfile

# Загрузка изображений из БД.
def load_images(*args):
    with sq.connect("dino.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    name TEXT NOT NULL,
                    high_score INTEGER
                    )""")
        str = ','.join('?' * len(args))
        cur.execute(f"SELECT image FROM images WHERE name IN ({str})", args)
        res = cur.fetchall()
    img = []
    for row in res:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            temp_file.write(row[0])
            temp_file_path = temp_file.name
        img.append(pygame.image.load(temp_file_path))
    return img

# Запись рекорда в БД.
def update_high_score(score, name):
    with sq.connect("dino.db") as con:
        cur = con.cursor()

        cur.execute("UPDATE users SET high_score = ? WHERE name = ?", (score, name))

# Загрузка рекорда.
def load_high_score(name):
    with sq.connect("dino.db") as con:
        cur = con.cursor()
        '''cur.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT NOT NULL,
            high_score INTEGER
            )""")'''
        cur.execute("""SELECT COUNT(*) FROM users WHERE name = ?""", (name,))
        result = cur.fetchone()[0]
        if result > 0:
            cur.execute("SELECT high_score FROM users WHERE name = ?", (name,))
            return cur.fetchone()[0]
        else:
            cur.execute("INSERT INTO users VALUES (?, 0)", (name,))
            return 0