import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def draw_line_rainbow(start_x=50, end_x=150):

    step = 0

    for color in rainbow_colors:
        start_point = sd.get_point(start_x+step, start_x)
        end_point = sd.get_point(end_x+step, end_x)
        sd.line(start_point=start_point, end_point=end_point, color=color, width=5)
        step += 5


def draw_rainbow(x=0, y=0, radius=700, width=6, game_tick=0,):
    step = 0

    for num, color in enumerate(rainbow_colors):

        start_point = sd.get_point(x, -y)
        sd.circle(center_position=start_point, radius=radius+step, color=color, width=width+1)
        step += width

    if game_tick % 3 == 0:
        rainbow_colors.append(rainbow_colors[0])
        rainbow_colors.remove(rainbow_colors[0])


if __name__ == '__main__':

    tick = 0
    step = 0

    while True:
        tick += 1
        sd.start_drawing()
        step += 5
        draw_rainbow(width=10, game_tick=tick)
        sd.finish_drawing()

        sd.sleep(0.01)

        if sd.user_want_exit():
            break
