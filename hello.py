from pico2d import *
import math

from pygame.draw import circle

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
count = 0
while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if count < 1200:
        if x <= 770 and y == 90:
            x += 2
        elif x >= 770 and y <= 550:
            y += 2
        elif 30 <= x and y >= 550:
            x -= 2
        elif x <= 30 and y >= 90:
            y -= 2
        count += 1
    if count >= 1200:
        x = 400 + 230 * math.cos((count - 1200) * 0.02)
        y = 300 + 230 * math.sin((count - 1200) * 0.02)
        count += 1
    if count >= 1430:
        count = 0
        x = 400
        y = 90
    delay(0.01)


close_canvas()