# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from CountUp.ui_countup_main import UiCountUp
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    ui_count_up = UiCountUp()
    ui_count_up.start()
    while True:
        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
