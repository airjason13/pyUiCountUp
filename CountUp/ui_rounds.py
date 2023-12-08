import pygame
from .global_def import *
from .icon_cord_def import *    # for icon cord(pos_x/pos_y)
from enum import IntEnum


class RoundNum(IntEnum):
    ROUND00 = 0
    ROUND01 = 1
    ROUND02 = 2
    ROUND03 = 3
    ROUND04 = 4
    ROUND05 = 5
    ROUND06 = 6
    ROUND07 = 7
    ROUND08 = 8
    ROUND09 = 9


ROUND_NUM_PNG_FILE_NAME_LIST = ['/01Game/RoundNum/0.png', '/01Game/RoundNum/1.png', '/01Game/RoundNum/2.png',
                           '/01Game/RoundNum/3.png', '/01Game/RoundNum/4.png', '/01Game/RoundNum/5.png',
                           '/01Game/RoundNum/6.png', '/01Game/RoundNum/7.png', '/01Game/RoundNum/8.png',
                           '/01Game/RoundNum/9.png']

ROUND_NUM_SLASH_PNG_FILE_NAME = '/01Game/RoundNum/Slash.png'


class UiRounds:
    def __init__(self, window, _pygame: pygame, material_folder_uri, _total_rounds=8, **kwargs):
        self.window = window
        self.pygame = _pygame
        self.material_folder_uri = material_folder_uri
        self.total_rounds = _total_rounds
        self.round_num_current = 1
        self.round_num_total = _total_rounds
        self.round_num_image = []
        self.total_round_num_image = None
        self.round_num_slash_image = None
        self.icon_init(self.round_num_total)

    def set_round(self, round_num: int):
        self.round_num_current = round_num

    def set_round_num_total(self, round_num_total: int):
        self.round_num_total = round_num_total

    def icon_init(self, total_round_num):
        '''current round number '''
        for i in range(total_round_num + 1):
            round_num_image = pygame.image.load("Image" + ROUND_NUM_PNG_FILE_NAME_LIST[i]).convert_alpha()
            self.round_num_image.append(round_num_image)

        '''total round number'''
        self.total_round_num_image = pygame.image.load(
            "Image" + ROUND_NUM_PNG_FILE_NAME_LIST[self.round_num_total]).convert_alpha()

        '''round number slash'''
        self.round_num_slash_image = pygame.image.load("Image" + ROUND_NUM_SLASH_PNG_FILE_NAME).convert_alpha()

    def draw_current_round_num(self):
        # print("self.round_num_current = ", self.round_num_current)
        self.window.blit(self.round_num_image[self.round_num_current],
                         self.pygame.rect.Rect(CurrentRoundNum.x, CurrentRoundNum.y,
                                               self.round_num_image[self.round_num_current].get_width(),
                                               self.round_num_image[self.round_num_current].get_height()))

    def draw_total_round_num(self):
        self.window.blit(self.round_num_slash_image,
                         self.pygame.rect.Rect(SlashRoundNum.x, SlashRoundNum.y,
                                               self.round_num_slash_image.get_width(),
                                               self.round_num_slash_image.get_height()))

        self.window.blit(self.total_round_num_image,
                         self.pygame.rect.Rect(TotalRoundNum.x, TotalRoundNum.y,
                                               self.total_round_num_image.get_width(),
                                               self.total_round_num_image.get_height()))

    def draw_round_info(self):
        self.draw_current_round_num()
        self.draw_total_round_num()
        if Performance_Test is True:
            self.round_num_current += 1
            if self.round_num_current > self.round_num_total:
                self.round_num_current = 0

