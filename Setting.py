import os
import xml.etree.ElementTree as ET

from CONST import Game, SubGame01
import Util

LED_MODE_MAX = 5  # 0 ~ 4

SETTING_FILENAME = "Settings.xml"

# ------------------------------------------------
NAME_GAME = "Game"
NAME_SUBGAME01 = "SubGame01"
NAME_GAME01_PLAYER_TTL = "Game01PlayerTtl"
NAME_COUNT_UP_PLAYER_TTL = "CountUpPlayerTtl"
NAME_BIG_BULL_PLAYER_TTL = "BigBullPlayerTtl"
NAME_CRICKET_PLAYER_TTL = "CricketPlayerTtl"

NAME_LED_MODE = "LedMode"

NAME_DARTBOARD_BRIGHTNESS = "DartboardBrightness"  # 靶面
NAME_HALO_BRIGHTNESS = "HaloBrightness"      # 光圈
NAME_SIDE_RED_BRIGHTNESS = "SideRedBrightness"
NAME_SIDE_GREEN_BRIGHTNESS = "SideGreenBrightness"
NAME_SIDE_ORANGE_BRIGHTNESS = "SideOrangeBrightness"
NAME_SIDE_BLUE_BRIGHTNESS = "SideBlueBrightness"

NAME_HALL_LED_RAINBOW_BREATH = "HallLedRainbowBreath"

NAME_VOLUME_EFFECT = "VolumeEffect"
NAME_VOLUME_MUSIC = "VolumeMusic"
NAME_VOLUME_KEY = "VolumeKey"

NAME_LOG_ENABLE = "LogEnable"
NAME_LOG2FILE_ENABLE = "Log2FileEnable"

NAME_SETTING_MENU = "SettingMenu"
NAME_MACHINE_TEST_MENU = "MachineTestMenu"

NAME_DART_RETURN_TIMES = "DartReturnTimes"

NAME_GAME_HAPPY_ADD_DART_NUM = "GameHappyAddDartNum"

NAME_LANGUAGE = "Language"

# ------------------------------------------------
DEFAULT_GAME = Game._01.value
DEFAULT_SUBGAME01 = SubGame01._501.value
DEFAULT_GAME01_PLAYER_TTL = 2  # 1 ~ 4
DEFAULT_COUNT_UP_PLAYER_TTL = 2  # 1 ~ 4
DEFAULT_BIG_BULL_PLAYER_TTL = 2  # 1 ~ 4
DEFAULT_CRICKET_PLAYER_TTL = 2  # 1 ~ 2

DEFAULT_LED_MODE = 2    # 0 ~ 4
DEFAULT_BRIGHTNESS = 3  # 0 ~ 6
DEFAULT_HALL_LED_RAINBOW_BREATH = 0  # 0 or 1

DEFAULT_VOLUME_EFFECT = 7  # 0 ~ 9
DEFAULT_VOLUME_MUSIC = 7   # 0 ~ 9
DEFAULT_VOLUME_KEY = 7     # 0 ~ 9

DEFAULT_LOG_ENABLE = 1  # 1 or 0
DEFAULT_LOG2FILE_ENABLE = 1  # 1 or 0

DEFAULT_SETTING_MENU = 0
DEFAULT_MACHINE_TEST_MENU = 0

DEFAULT_DART_RETURN_TIMES = 9  # 9, 12, 15

DEFAULT_GAME_HAPPY_ADD_DART_NUM = 5  # 5 or 10

DEFAULT_LANGUAGE = 0

# ------------------------------------------------
Game = DEFAULT_GAME
SubGame01 = DEFAULT_SUBGAME01
Game01PlayerTtl = DEFAULT_GAME01_PLAYER_TTL
CountUpPlayerTtl = DEFAULT_COUNT_UP_PLAYER_TTL
BigBullPlayerTtl = DEFAULT_BIG_BULL_PLAYER_TTL
CricketPlayerTtl = DEFAULT_CRICKET_PLAYER_TTL

LedMode = DEFAULT_LED_MODE

DartboardBrightness = DEFAULT_BRIGHTNESS
HaloBrightness = DEFAULT_BRIGHTNESS
SideRedBrightness = DEFAULT_BRIGHTNESS
SideGreenBrightness = DEFAULT_BRIGHTNESS
SideOrangeBrightness = DEFAULT_BRIGHTNESS
SideBlueBrightness = DEFAULT_BRIGHTNESS

HallLedRainbowBreath = DEFAULT_HALL_LED_RAINBOW_BREATH

VolumeEffect = DEFAULT_VOLUME_EFFECT
VolumeMusic = DEFAULT_VOLUME_MUSIC
VolumeKey = DEFAULT_VOLUME_KEY

LogEnable = DEFAULT_LOG_ENABLE
Log2FileEnable = DEFAULT_LOG2FILE_ENABLE

SettingMenu = DEFAULT_SETTING_MENU
MachineTestMenu = DEFAULT_MACHINE_TEST_MENU

DartReturnTimes = DEFAULT_DART_RETURN_TIMES

GameHappyAddDartNum = DEFAULT_GAME_HAPPY_ADD_DART_NUM

Language = DEFAULT_LANGUAGE

# ------------------------------------------------
def Init():
    if os.path.isfile(SETTING_FILENAME):
        #print("{} Existent, Read Settings File".format(SETTING_FILENAME))
        ReadFile()
    else:
        #print("{} Inexistent, Write Default".format(SETTING_FILENAME))
        WriteFile()

def WriteFile():
    Util.PRINT("Write Settings File")

    root = ET.Element("Root")

    ET.SubElement(root, "Setting", name=NAME_GAME).text = str(Game)
    ET.SubElement(root, "Setting", name=NAME_SUBGAME01).text = str(SubGame01)
    ET.SubElement(root, "Setting", name=NAME_GAME01_PLAYER_TTL).text = str(Game01PlayerTtl)
    ET.SubElement(root, "Setting", name=NAME_COUNT_UP_PLAYER_TTL).text = str(CountUpPlayerTtl)
    ET.SubElement(root, "Setting", name=NAME_BIG_BULL_PLAYER_TTL).text = str(BigBullPlayerTtl)
    ET.SubElement(root, "Setting", name=NAME_CRICKET_PLAYER_TTL).text = str(CricketPlayerTtl)

    ET.SubElement(root, "Setting", name=NAME_LED_MODE).text = str(LedMode)

    ET.SubElement(root, "Setting", name=NAME_DARTBOARD_BRIGHTNESS).text = str(DartboardBrightness)
    ET.SubElement(root, "Setting", name=NAME_HALO_BRIGHTNESS).text = str(HaloBrightness)
    ET.SubElement(root, "Setting", name=NAME_SIDE_RED_BRIGHTNESS).text = str(SideRedBrightness)
    ET.SubElement(root, "Setting", name=NAME_SIDE_GREEN_BRIGHTNESS).text = str(SideGreenBrightness)
    ET.SubElement(root, "Setting", name=NAME_SIDE_ORANGE_BRIGHTNESS).text = str(SideOrangeBrightness)
    ET.SubElement(root, "Setting", name=NAME_SIDE_BLUE_BRIGHTNESS).text = str(SideBlueBrightness)

    ET.SubElement(root, "Setting", name=NAME_HALL_LED_RAINBOW_BREATH).text = str(HallLedRainbowBreath)

    ET.SubElement(root, "Setting", name=NAME_VOLUME_EFFECT).text = str(VolumeEffect)
    ET.SubElement(root, "Setting", name=NAME_VOLUME_MUSIC).text = str(VolumeMusic)
    ET.SubElement(root, "Setting", name=NAME_VOLUME_KEY).text = str(VolumeKey)

    ET.SubElement(root, "Setting", name=NAME_LOG_ENABLE).text = str(LogEnable)
    ET.SubElement(root, "Setting", name=NAME_LOG2FILE_ENABLE).text = str(Log2FileEnable)

    ET.SubElement(root, "Setting", name=NAME_SETTING_MENU).text = str(SettingMenu)
    ET.SubElement(root, "Setting", name=NAME_MACHINE_TEST_MENU).text = str(MachineTestMenu)

    ET.SubElement(root, "Setting", name=NAME_DART_RETURN_TIMES).text = str(DartReturnTimes)
    
    ET.SubElement(root, "Setting", name=NAME_GAME_HAPPY_ADD_DART_NUM).text = str(GameHappyAddDartNum)

    ET.SubElement(root, "Setting", name=NAME_LANGUAGE).text = str(Language)

    tree = ET.ElementTree(root)
    tree.write(SETTING_FILENAME)

def ReadFile():
    global Game, SubGame01, Game01PlayerTtl, CountUpPlayerTtl, BigBullPlayerTtl, CricketPlayerTtl, LedMode, DartboardBrightness, HaloBrightness, SideRedBrightness,\
           SideGreenBrightness, SideOrangeBrightness, SideBlueBrightness, VolumeEffect, VolumeMusic, VolumeKey, LogEnable, Log2FileEnable, SettingMenu,\
           MachineTestMenu, DartReturnTimes, GameHappyAddDartNum, Language
    
    tree = ET.parse(SETTING_FILENAME)
    root = tree.getroot()
    
    for child in root:
        name = child.get("name")
        text = child.text

        if name == NAME_GAME:
            Game = int(text)
        elif name == NAME_SUBGAME01:
            SubGame01 = int(text)
        elif name == NAME_GAME01_PLAYER_TTL:
            Game01PlayerTtl = int(text)
        elif name == NAME_COUNT_UP_PLAYER_TTL:
            CountUpPlayerTtl = int(text)
        elif name == NAME_BIG_BULL_PLAYER_TTL:
            BigBullPlayerTtl = int(text)
        elif name == NAME_CRICKET_PLAYER_TTL:
            CricketPlayerTtl = int(text)

        elif name == NAME_LED_MODE:
            LedMode = int(text)

        elif name == NAME_DARTBOARD_BRIGHTNESS:
            DartboardBrightness = int(text)
        elif name == NAME_HALO_BRIGHTNESS:
            HaloBrightness = int(text)
        elif name == NAME_SIDE_RED_BRIGHTNESS:
            SideRedBrightness = int(text)
        elif name == NAME_SIDE_GREEN_BRIGHTNESS:
            SideGreenBrightness = int(text)
        elif name == NAME_SIDE_ORANGE_BRIGHTNESS:
            SideOrangeBrightness = int(text)
        elif name == NAME_SIDE_BLUE_BRIGHTNESS:
            SideBlueBrightness = int(text)

        elif name == NAME_HALL_LED_RAINBOW_BREATH:
            HallLedRainbowBreath = int(text)

        elif name == NAME_VOLUME_EFFECT:
            VolumeEffect = int(text)
        elif name == NAME_VOLUME_MUSIC:
            VolumeMusic = int(text)
        elif name == NAME_VOLUME_KEY:
            VolumeKey = int(text)

        elif name == NAME_LOG_ENABLE:
            LogEnable = int(text)
        elif name == NAME_LOG2FILE_ENABLE:
            Log2FileEnable = int(text)

        elif name == NAME_SETTING_MENU:
            SettingMenu = int(text)
        elif name == NAME_MACHINE_TEST_MENU:
            MachineTestMenu = int(text)

        elif name == NAME_DART_RETURN_TIMES:
            DartReturnTimes = int(text)

        elif name == NAME_GAME_HAPPY_ADD_DART_NUM:
            GameHappyAddDartNum = int(text)

        elif name == NAME_LANGUAGE:
            Language = int(text)

        print("{} = {}".format(name, text))
