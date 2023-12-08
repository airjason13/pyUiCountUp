import time
import pygame
import threading
from .ui_background import UiAnimatedBackground
from .ui_fix_icon import UiFixIcon
from .ui_rounds import UiRounds
from .ui_players import UiPlayers

class UiCountUp:
    def __init__(self,  **kwargs):
        print("UiCountUp Init")
        pygame.init()
        self.win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.SCALED, vsync=1)
        pygame.display.set_caption("Venom Test")

        ''' Handle BackGround Gif Image'''
        self.ui_background = UiAnimatedBackground(self.win, pygame, "Image/GIF/Background/stock-foot.gif")
        self.ui_background.start_drawing()

        '''Handle Fix Icon Image'''
        self.fix_icon = UiFixIcon(self.win, pygame, "Image")

        '''Handle Round Info'''
        self.ui_round_info = UiRounds(self.win, pygame, "Image")

        '''Handle Player Info'''
        self.ui_player_info = UiPlayers(self.win, pygame, "Image")

        self.update_screen_thread = threading.Thread(target=self.update_screen)

    def start(self):
        self.update_screen_thread.start()

    def update_screen(self):
        while True:

            '''draw back ground'''
            self.ui_background.draw()

            '''draw fix icon'''
            self.fix_icon.draw_all()

            '''draw round info'''
            self.ui_round_info.draw_round_info()

            '''draw player info(score?)'''
            self.ui_player_info.draw_all()

            pygame.display.flip()
            pygame.display.update()
            time.sleep(0.001)



