from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 800
while (x > 0):
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x -= 2
    delay(0.01)

close_canvas()
