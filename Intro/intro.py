import pygame as pg

# some shapes
RECT = (10, 10, 50, 50)

# some colors
GREEN = (0, 255, 0)



pg.init()
WIN = pg.display.set_mode((500, 500))
pg.display.set_caption("Hello Game.")

running = True

while(running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            print("Quitting.")
    
    pg.draw.rect(WIN, GREEN, RECT)
    pg.display.update()
    