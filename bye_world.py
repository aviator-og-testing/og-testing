# 🌈✨ SHARE THIS WITH 10 FRIENDS OR YOU'LL HAVE BAD LUCK ✨🌈

import time
from colorama import Fore, Style, init

init(autoreset=True)

def print_bye_world():
    """Print Bye World with maximum early-2010s Facebook aesthetic"""

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    border_top = "✨💕🌟👋😭" * 10
    border_bottom = "😭👋🌟💕✨" * 10

    print("\n" * 2)
    print(border_top)
    print(border_top)
    time.sleep(0.3)

    for i in range(3):
        line = ""
        text = "✨💕 BYE WORLD 💕✨"
        for j, char in enumerate(text):
            color = colors[(i + j) % len(colors)]
            line += color + char

        print(" " * 20 + line + Style.RESET_ALL)
        time.sleep(0.4)

    print("\n")
    sparkle_line = "✨ " * 30
    print(Fore.YELLOW + sparkle_line + Style.RESET_ALL)
    time.sleep(0.3)

    heart_line = "💕 " * 30
    print(Fore.MAGENTA + heart_line + Style.RESET_ALL)
    time.sleep(0.3)

    star_line = "🌟 " * 30
    print(Fore.CYAN + star_line + Style.RESET_ALL)
    time.sleep(0.3)

    wave_line = "👋 " * 30
    print(Fore.GREEN + wave_line + Style.RESET_ALL)
    time.sleep(0.3)

    cry_line = "😭 " * 30
    print(Fore.BLUE + cry_line + Style.RESET_ALL)
    time.sleep(0.3)

    print("\n")
    print(border_bottom)
    print(border_bottom)
    print("\n" * 2)

if __name__ == "__main__":
    print_bye_world()
    exit(0)
