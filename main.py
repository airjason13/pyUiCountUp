# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from CountUp.ui_countup_main import UiCountUp
import time
import Sound as Sound


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    Sound.SoundInit()
    ui_count_up = UiCountUp(_sound=Sound)

    ui_count_up.start(2)
    while True:
        time.sleep(10)
        ui_count_up.quit()
        time.sleep(1)
        exit(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
