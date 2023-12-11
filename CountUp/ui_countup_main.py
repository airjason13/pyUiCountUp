import time
import pygame
import threading
from .ui_background import UiAnimatedBackground
from .ui_fix_icon import UiFixIcon
from .ui_rounds import UiRounds
from .ui_players import UiPlayers
from .func_countup import FuncCountUp
from .global_def import *
import Sound as Sound
import CONST as CONST


class UiCountUp:
    def __init__(self,  _sound=None, **kwargs):
        log.debug("UiCountUp Init")
        pygame.init()
        self.sound = _sound
        self.win = pygame.display.set_mode((1920, 1080),
                                           pygame.FULLSCREEN | pygame.SCALED | pygame.HWSURFACE | pygame.DOUBLEBUF,
                                           vsync=1)
        self.clock = pygame.time.Clock()

        self.is_game_over = False
        self.quit_update_screen = False
        pygame.display.set_caption("Venom Test")

        ''' current round/current player/current dart'''
        self.current_round = 0
        self.current_player = 0
        self.current_dart = 0

        '''key event initial'''
        self.ignore_all_events_upon_enter_new_round_timer = None
        self.ignore_all_event_upon_Enter_new_round = False

        self.handle_shoot_dart_event = False
        self.handle_key_event = False

        ''' Handle BackGround Gif Image'''
        self.ui_background = UiAnimatedBackground(self.win, pygame, "Image/GIF/Background/stock-foot.gif")
        self.ui_background.start_drawing()

        '''Handle Fix Icon Image'''
        self.fix_icon = UiFixIcon(self.win, pygame, "Image")

        '''Handle Round Info'''
        self.ui_round_info = UiRounds(self.win, pygame, "Image")

        '''Handle Player Info'''
        self.ui_player_info = UiPlayers(self.win, pygame, "Image", 4)

        '''Handle Ui Update Screen'''
        self.update_screen_thread = threading.Thread(target=self.update_screen)

        self.func_countup = FuncCountUp(self, self.ui_round_info, self.ui_player_info)

        ''' For Sound Test'''
        self.test_play_sound()

    def start(self, _player_num):
        self.ui_player_info.set_player_num(_player_num)
        self.update_screen_thread.start()

    def uart_adc_event(self, _dbaId):
        print("dbaId = ", _dbaId)
        if self.ignore_all_event_upon_Enter_new_round:
            log.debug("ignore_all_event_upon_Enter_new_round")
            return False

        if self.handle_shoot_dart_event:
            log.debug("handle_shoot_dart_event")
            return False

        if self.handle_key_event:
            log.debug("handle_key_event")
            return False
        else:
            self.handle_key_event = True

        # self.func_countup.

    def quit(self):
        self.quit_update_screen = True
        pygame.quit()

    def test_play_sound(self):
        if not pygame.mixer.get_init():
            print("sound not init!\n")
            return

        self.sound.PlayInfiniteHall()

    def ui_callback(self, **kwargs):
        log.debug("%s", kwargs)

    def key_press_event(self, key):
        log.debug("")
        if self.ignore_all_event_upon_Enter_new_round:
            log.debug("ignore_all_event_upon_Enter_new_round")
            return False

        if self.handle_shoot_dart_event:
            log.debug("handle_shoot_dart_event")
            return False

        if self.handle_key_event:
            log.debug("handle_key_event")
            return False
        else:
            self.handle_key_event = True

        Sound.StopEffect()
        if key == CONST.Key.DART_BACK:
            Sound.PlayBack()
            self.func_countup.got_back_key_event()
        elif key == CONST.Key.DART_PASS:
            Sound.PlayKey()
            self.func_countup.got_pass_key_event()
        elif key == CONST.Key.ENTER:
            Sound.PlayNext()
            self.func_countup.got_nex_key_event()
        elif key == CONST.Key.DART_BACK2LAST_PLAYER:
            Sound.PlayBack()
            self.func_countup.got_back_2_last_player_by_hold_back_key_event()
        else:
            self.handle_key_event = False
            log.debug("HandlingKeyEvent=False")
            # Log2File.Write("HandlingKeyEvent=False")
            return False
        return True

    def update_screen(self):
        while 1:
            if self.quit_update_screen is True:
                break
            # self.clock.tick(60)
            # print(self.clock.get_fps())
            '''draw back ground'''
            self.ui_background.draw()

            '''draw fix icon'''
            self.fix_icon.draw_all()

            '''draw round info'''
            self.ui_round_info.draw_round_info()

            '''draw player info(score?)'''
            self.ui_player_info.draw_all()

            # pygame.display.flip()
            pygame.display.update()
            # time.sleep(0.001)



