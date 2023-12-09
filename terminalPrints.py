from constants import COLORS, BG_COLORS

def print_title (title):
    print(
            f"{COLORS['purple']}==========| {title} |=========={COLORS['reset']}")

def print_colored_text(text, color, end="\n"):
    if color in COLORS.keys():
        print(f"{COLORS[color]}{text}{COLORS['reset']}", end=end)
    else:
        print(text)

def print_text_with_bg(text, color, end="\n"):
    if color in BG_COLORS.keys():
        print(f"{BG_COLORS[color]}{text}{COLORS['reset']}", end=end)
    else:
        print(text)

def print_progress(status_vector):
    print("Progreso: ", end="")
    current_done = 0
    for status in status_vector:
        if status == 0:
            print("■", end="")
        elif status == 1:
            print_colored_text("■", "green", end="")
            current_done += 1
        elif status == -1:
            print_colored_text("■", "red", end="")
            current_done += 1
    print(f" {current_done}/{len(status_vector)}\n")
