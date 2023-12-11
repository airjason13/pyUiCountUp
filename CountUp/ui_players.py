import pygame
from .global_def import *
from .icon_cord_def import *    # for icon cord(pos_x/pos_y)
from enum import IntEnum

Center_Player_Icon_PNG_File_Name_List = ['/Player/CenterPlayer1.png', '/Player/CenterPlayer2.png',
                                         '/Player/CenterPlayer3.png', '/Player/CenterPlayer4.png']

Player_Red_Background_PNG_File_Name = '/Player/PlayerRedBackground.png'
Player_Green_Background_PNG_File_Name = '/Player/PlayerGreenBackground.png'
Player_Orange_Background_PNG_File_Name = '/Player/PlayerOrangeBackground.png'
Player_Blue_Background_PNG_File_Name = '/Player/PlayerBlueBackground.png'
Bottom_Player_Name_Enable_PNG_File_Name_List = ['/Player/BottomPlayer1Enable.png', '/Player/BottomPlayer2Enable.png',
                                                '/Player/BottomPlayer3Enable.png', '/Player/BottomPlayer4Enable.png']

Bottom_Player_Name_Disable_PNG_File_Name_List = ['/Player/BottomPlayer1Disable.png', '/Player/BottomPlayer2Disable.png',
                                                 '/Player/BottomPlayer3Disable.png', '/Player/BottomPlayer4Disable.png']


Bottom_Player_Background_Cord_List = [PlayerBackground01, PlayerBackground02, PlayerBackground03, PlayerBackground04]
Bottom_Player_Name_Cord_List = [BottomPlayerName01, BottomPlayerName02, BottomPlayerName03, BottomPlayerName04]


class UiPlayers:
    def __init__(self, window, _pygame: pygame, material_folder_uri, _max_players=4, _max_darts=4, **kwargs):
        self.window = window
        self.pygame = _pygame
        self.material_folder_uri = material_folder_uri

        self.max_players = _max_players
        self.player_num = _max_players
        self.current_player = 0
        self.max_darts = _max_darts
        self.darts = Dart(self.max_darts)
        self.center_player_icon_images = []
        self.bottom_player_name_enable_icon_images = []
        self.player_red_background_png_image = None
        self.icon_init()

    def icon_init(self):
        for i in range(self.max_players):
            center_player_icon_image = pygame.image.load(
                'Image' + Center_Player_Icon_PNG_File_Name_List[i]).convert_alpha()
            self.center_player_icon_images.append(center_player_icon_image)

            bottom_player_name_enable_images = pygame.image.load(
                'Image' + Bottom_Player_Name_Enable_PNG_File_Name_List[i]).convert_alpha()
            self.bottom_player_name_enable_icon_images.append(bottom_player_name_enable_images)

        self.player_red_background_png_image = pygame.image.load(
            "Image" + Player_Red_Background_PNG_File_Name).convert_alpha()

    def set_player_num(self, _player_num):
        self.player_num = _player_num

    def draw_center_player_icon(self):
        self.window.blit(self.center_player_icon_images[self.current_player],
                         self.pygame.rect.Rect(CenterPlayerIcon.x, CenterPlayerIcon.y,
                                               self.center_player_icon_images[self.current_player].get_width(),
                                               self.center_player_icon_images[self.current_player].get_height()))

    def draw_bottom_player_info(self):
        self.window.blit(self.player_red_background_png_image,
                         self.pygame.rect.Rect(Bottom_Player_Background_Cord_List[self.current_player].x,
                                               Bottom_Player_Background_Cord_List[self.current_player].y,
                                               self.player_red_background_png_image.get_width(),
                                               self.player_red_background_png_image.get_height()))
        for i in range(self.max_players):
            self.window.blit(self.bottom_player_name_enable_icon_images[i],
                             self.pygame.rect.Rect(Bottom_Player_Name_Cord_List[i].x,
                                                   Bottom_Player_Name_Cord_List[i].y,
                                                   self.bottom_player_name_enable_icon_images[i].get_width(),
                                                   self.bottom_player_name_enable_icon_images[i].get_height()))

    def draw_all(self):
        # print("self.current_player : ", self.current_player)
        self.draw_center_player_icon()
        self.draw_bottom_player_info()
        if Performance_Test is True:
            self.current_player += 1
            if self.current_player >= self.max_players:
                self.current_player = 0

class Dart:
    def __init__(self, _darts_total):
        self.darts_total = _darts_total
        self.current_dart = 0
        self.darts_score = [0] * self.darts_total

    def reset(self):
        self.current_dart = 0
        self.darts_score.clear()
        self.darts_score = [0] * self.darts_total

