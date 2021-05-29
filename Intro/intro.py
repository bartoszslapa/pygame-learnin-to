import pygame as pg

pg.init()
win = pg.display.set_mode((500, 500))
pg.display.set_caption("Hello Gro.")

running = True

while(running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            print("Quitting.")