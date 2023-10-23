from constants import COLORS

def print_title (title):
    print(
            f"{COLORS['purple']}==========| {title} |=========={COLORS['reset']}");

def print_colored_text(text, color, end="\n"):
    if color in COLORS.keys():
        print(f"{COLORS[color]}{text}{COLORS['reset']}", end=end);
    else:
        print(text);