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
    color_line = (255, 255, 255)
    top_line = pg.draw.aaline(display, color_line,
                              [10, 10],
                              [410, 10])
    bot_line = pg.draw.aaline(display, color_line,
                              [10, 890],
                              [410, 890])
    line_under_name = pg.draw.line(display, color_line,
                                   [410, 90],
                                   [650, 90], 3)
    line_under_score = pg.draw.line(display, color_line,
                                    [410, 210],
                                    [650, 210], 3)
    line_dont_know_1 = pg.draw.line(display, color_line,
                                    [410, 330],
                                    [650, 330], 3)
    line_dont_know_2 = pg.draw.line(display, color_line,
                                    [410, 610],
                                    [650, 610], 3)

    for i in range(10, 450, 40):
        line = pg.draw.line(display, color_line, [i, 10], [i, 890], 1)
    for j in range(50, 890, 40):
        line = pg.draw.line(display, color_line, [10, j], [410, j], 1)


def run_game():
    game = True
    score = 0
    font_type_1 = pg.font.Font('Baron Neue.otf', 25)
    white = (255, 255, 255)
    text_1 = font_type_1.render('tetrows', True, white)
    font_type_2 = pg.font.Font('Baron Neue.otf', 20)
    text_2 = font_type_2.render('score: 0', True, white)
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
        display.blit(text_1, (475, 40))
        display.blit(text_2, (420, 143))
        pg.display.update()

        # Установка фона окна
        display.fill((22, 7, 115))
        coord_system()


run_game()
