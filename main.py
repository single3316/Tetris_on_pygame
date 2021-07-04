import pygame as pg

pg.init()

display_width = 650
display_height = 900

display = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Tetrows')

button_sound = pg.mixer.Sound('button.wav')

icon = pg.image.load('icon.ico')


def quit_game():
    pg.quit()
    quit()


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_button(self, x, y, message, action=None):
        click = pg.mouse.get_pressed()
        rect = pg.draw.rect(display, (222, 120, 31), (x, y, self.width, self.height))
        if click[0] == 1 and action is not None:
            pg.mixer.Sound.play(button_sound)
            pg.time.delay(300)
            action()
        wrote_text(message, x + 60, y + 17, 30)


def draw_grid():
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

    button_pause = Button(210, 60)
    button_menu = Button(210, 60)

    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
        wrote_text('tetrows', 475, 40, 25)
        wrote_text('score: ' + str(score), 420, 143, 20)
        button_pause.draw_button(425, 820, 'pause')
        button_menu.draw_button(425, 700, 'menu')

        pg.display.update()

        display.fill((22, 7, 115))
        draw_grid()


def wrote_text(message, x, y, font_size, font_type='Baron Neue.otf', font_color=(255, 255, 255), ):
    font_type = pg.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


run_game()
