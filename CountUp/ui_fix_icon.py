import pygame
from .global_def import *
from .icon_cord_def import *    # for icon cord(pos_x/pos_y)


'''Image File Uri'''
Title_CountUp_PNG_File_Name = '/CountUp/CountUp.png'
Hint_CountUp_PNG_File_Name = '/CountUp/MainBackground1.png'
Round_Frame_CountUp_PNG_File_Name = '/01Game/RoundFrame.png'
Round_Score_TC_CountUp_PNG_File_Name = '/01Game/RoundScore_TC.png'
Round_Score_CountUp_PNG_File_Name = '/01Game/RoundScore.png'
Round_Bar_Frame_Red_CountUp_PNG_File_Name = '/Player/RoundBarFrameRed.png'
Round_Bar_Frame_Green_CountUp_PNG_File_Name = '/Player/RoundBarFrameGreen.png'
Round_Bar_Frame_Orange_CountUp_PNG_File_Name = '/Player/RoundBarFrameOrange.png'
Round_Bar_Frame_Blue_CountUp_PNG_File_Name = '/Player/RoundBarFrameBlue.png'
Three_Dim_Darts_Frame_CountUp_PNG_File_Name = '/01Game/3DartsFrame.png'
Dart_Result_CountUp_PNG_File_Name = '/01Game/DartsResults.png'
Dart_Result_TC_CountUp_PNG_File_Name = '/01Game/DartsResults_TC.png'
Player_Bar_Frame_CountUp_PNG_File_Name = '/01Game/PlayerBarFrame.png'
LetUsStart_CountUp_PNG_File_Name = '/01Game/LetUsStart.png'
LetsParty_CountUp_PNG_File_Name = '/HappyAdd/LetsParty.png'
Dart_Circle_Icon_PNG_File_Name = '/01Game/DartCircleIcon.png'
Player_Background_PNG_File_Name = '/01Game/PlayerBackground.png'
Player_Decorative_Pattern_PNG_File_Name = '/01Game/PlayerDecorativePattern.png'


Player_Background_Frame_Cord_List = [PlayerBackground01, PlayerBackground02, PlayerBackground03, PlayerBackground04]
Player_Decorative_Pattern_Cord_Lists = [PlayerDecorativePattern01, PlayerDecorativePattern02,
                                        PlayerDecorativePattern03, PlayerDecorativePattern04]
'''
Fix Icon include the Title, the Hint, 
'''


class UiFixIcon:

    def __init__(self, window, _pygame: pygame, material_folder_uri, **kwargs):
        self.window = window
        self.pygame = _pygame
        self.material_folder_uri = material_folder_uri

        ''' Image Init '''
        self.title_png_image = pygame.image.load("Image" + Title_CountUp_PNG_File_Name).convert_alpha()
        self.hint_png_image = pygame.image.load("Image" + Hint_CountUp_PNG_File_Name).convert_alpha()
        self.round_frame_png_image = pygame.image.load("Image" + Round_Frame_CountUp_PNG_File_Name).convert_alpha()
        self.round_score_tc_png_image = pygame.image.load(
            "Image" + Round_Score_TC_CountUp_PNG_File_Name).convert_alpha()
        self.round_bar_frame_red_png_image = pygame.image.load(
            "Image" + Round_Bar_Frame_Red_CountUp_PNG_File_Name).convert_alpha()
        self.three_dim_darts_frame_png_image = pygame.image.load(
            "Image" + Three_Dim_Darts_Frame_CountUp_PNG_File_Name).convert_alpha()
        self.dart_results_png_image = pygame.image.load(
            "Image" + Dart_Result_CountUp_PNG_File_Name).convert_alpha()
        self.dart_results_tc_png_image = pygame.image.load(
            "Image" + Dart_Result_TC_CountUp_PNG_File_Name).convert_alpha()
        self.player_bar_frame_png_image = pygame.image.load(
            "Image" + Player_Bar_Frame_CountUp_PNG_File_Name).convert_alpha()
        self.lets_party_png_image = pygame.image.load(
            "Image" + LetsParty_CountUp_PNG_File_Name).convert_alpha()
        self.dart_circle_icon_png_image = pygame.image.load(
            "Image" + Dart_Circle_Icon_PNG_File_Name).convert_alpha()
        self.player_background_png_image = pygame.image.load(
            "Image" + Player_Background_PNG_File_Name).convert_alpha()
        self.player_decorative_pattern_png_image = pygame.image.load(
            "Image" + Player_Decorative_Pattern_PNG_File_Name).convert_alpha()



    def draw_all(self):
        self.window.blit(self.title_png_image,
                         self.pygame.rect.Rect(CountUpTitlePos.x, CountUpTitlePos.y,
                                               self.title_png_image.get_width(), self.title_png_image.get_height()))

        self.window.blit(self.hint_png_image,
                         self.pygame.rect.Rect(CountUpGameHint.x, CountUpGameHint.y,
                                               self.hint_png_image.get_width(), self.hint_png_image.get_height()))

        self.window.blit(self.round_frame_png_image,
                         self.pygame.rect.Rect(CountUpRoundFrame.x, CountUpRoundFrame.y,
                                               self.round_frame_png_image.get_width(),
                                               self.round_frame_png_image.get_height()))

        self.window.blit(self.round_score_tc_png_image,
                         self.pygame.rect.Rect(CountUpRoundScoreTC.x, CountUpRoundScoreTC.y,
                                               self.round_score_tc_png_image.get_width(),
                                               self.round_score_tc_png_image.get_height()))

        self.window.blit(self.round_bar_frame_red_png_image,
                         self.pygame.rect.Rect(CountUpRoundBarFrameRed.x, CountUpRoundBarFrameRed.y,
                                               self.round_bar_frame_red_png_image.get_width(),
                                               self.round_bar_frame_red_png_image.get_height()))

        self.window.blit(self.three_dim_darts_frame_png_image,
                         self.pygame.rect.Rect(ThreeDimDartsFrame.x, ThreeDimDartsFrame.y,
                                               self.three_dim_darts_frame_png_image.get_width(),
                                               self.three_dim_darts_frame_png_image.get_height()))

        self.window.blit(self.dart_results_tc_png_image,
                         self.pygame.rect.Rect(DartResult.x, DartResult.y,
                                               self.dart_results_tc_png_image.get_width(),
                                               self.dart_results_tc_png_image.get_height()))

        self.window.blit(self.player_bar_frame_png_image,
                         self.pygame.rect.Rect(PlayerBarFrame.x, PlayerBarFrame.y,
                                               self.player_bar_frame_png_image.get_width(),
                                               self.player_bar_frame_png_image.get_height()))

        self.window.blit(self.lets_party_png_image,
                         self.pygame.rect.Rect(LetsParty.x, LetsParty.y,
                                               self.lets_party_png_image.get_width(),
                                               self.lets_party_png_image.get_height()))

        self.window.blit(self.dart_circle_icon_png_image,
                         self.pygame.rect.Rect(DartCircleIcon.x, DartCircleIcon.y,
                                               self.dart_circle_icon_png_image.get_width(),
                                               self.dart_circle_icon_png_image.get_height()))

        for i in range(MAX_PLAYER):
            self.window.blit(self.player_background_png_image,
                             self.pygame.rect.Rect(Player_Background_Frame_Cord_List[i].x,
                                                   Player_Background_Frame_Cord_List[i].y,
                                                   self.player_background_png_image.get_width(),
                                                   self.player_background_png_image.get_height()))

        for i in range(MAX_PLAYER):
            self.window.blit(self.player_decorative_pattern_png_image,
                             self.pygame.rect.Rect(Player_Decorative_Pattern_Cord_Lists[i].x,
                                                   Player_Decorative_Pattern_Cord_Lists[i].y,
                                                   self.player_decorative_pattern_png_image.get_width(),
                                                   self.player_decorative_pattern_png_image.get_height()))

