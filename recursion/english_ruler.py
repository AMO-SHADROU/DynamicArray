def draw_line(tick_length, tick_label=""):
    """Draws a line with given tick length (followed by optional tick label)"""
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval with given center length"""
    if center_length > 0:
        draw_interval(center_length - 1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length - 1)  # recursively draw bottom ticks


def draw_ruler(num_inches, major_length):
    draw_line(major_length, "0")
    for i in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i))


draw_ruler(1, 5)
