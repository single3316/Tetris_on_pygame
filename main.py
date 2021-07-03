import pygame as pg

pg.init()

display_width = 600
display_height = 900

display = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Tetris')

icon = pg.image.load('icon.ico')


def quit_game():
    pg.quit()
    quit()


def coord_system():
    color_line = (0, 0, 0)
    top_line = pg.draw.aaline(display, color_line,
                              [0, 10],
                              [800, 10])
    bot_line = pg.draw.aaline(display, color_line,
                              [0, 890],
                              [800, 890])

    for i in range(40, 440, 40):
        line = pg.draw.line(display, color_line, [i, 10], [i, 890], 1)
    for j in range(50, 890, 40):
        line = pg.draw.line(display, color_line, [0, j], [420, j], 1)


def run_game():
    game = True

    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()

        # Установка фона окна
        display.fill((0, 255, 255))
        coord_system()
        pg.display.update()


run_game()
