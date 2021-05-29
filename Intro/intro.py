import pygame as pg

# some shapes
RECT = (10, 10, 50, 50)

# some colors
GREEN = (0, 255, 0)


# init pygame modules
pg.init()

# init a window
WIN = pg.display.set_mode((500, 500))
pg.display.set_caption("Hello Game.")

# main loop
running = True
while running:
    #event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            print("Quitting.")
    
    # draw a green rectangle to window WIN and update the window
    pg.draw.rect(WIN, GREEN, RECT)
    pg.display.update()
    