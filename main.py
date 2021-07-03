import pygame as pg

pg.init()

display_width = 650
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
                              [10, 10],
                              [410, 10])
    bot_line = pg.draw.aaline(display, color_line,
                              [10, 890],
                              [410, 890])

    for i in range(10, 450, 40):
        line = pg.draw.line(display, color_line, [i, 10], [i, 890], 1)
    for j in range(50, 890, 40):
        line = pg.draw.line(display, color_line, [10, j], [410, j], 1)


def run_game():
    game = True
    score = 0

    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()

        # Установка фона окна
        display.fill((0, 255, 255))
        coord_system()
        pg.display.update()


run_game()
