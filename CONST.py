from enum import Enum, auto

VER_MAJOR = 1
VER_MINOR = 0
VER_YEAR = 2023
VER_MONTH = 10
VER_DAY = 5

# 2023-05-18 -------------------------------------------------------------------
# New Light Adjust Menu 20230504
# One more LED mode (SixFullRgbColors) in HALL
# Show 'Miss' shootdart icon in ENG-MODE

# 2023-05-22 -------------------------------------------------------------------
# Add Dartboard Area String into IDLE ADC CH in ENG-MODE
# Show 'Miss' shootdart icon in Dartboard Test Menu

# 2023-08-22 -------------------------------------------------------------------
# Porting Individual Main Background Picture for Every Player into Game01
# Modified Files: main.py , Ui01Game.py
# Added Files: ./Image/Player/GameBackgroundPlayer1~4.png

# 2023-08-22_WhiteHorseMP4Test -------------------------------------------------
# Porting White Horse MP4 Test into Cricket
# Modified Files: main.py , Util.py , UiCricket.py
# Added Files: ./MP4/WhiteHorse.mp4

# 2023-08-22_Show_ThrowDarts ---------------------------------------------------
# Show ThrowDarts.png into Game01 when Event Acceptable
# Add Log into IgnoreAllEventsUponEnterNewRoundTimeout() and StartIgnoreAllEventsUponEnterNewRoundTimer() of Game01
# Modified Files: Ui01Game.py , CONST.py
# Added Files: ./Other/ThrowDarts.png

# 2023-10-05 -------------------------------------------------------------------
# Try to add "Big Bull" game, based on codebase EDB22NTA0
# It's the first draft version for "Big Bull" game test

#-------------------------------------------------------------------------------

# Sensor Board Info (Get by UART)
SB_PROJECT_NAME = ''
SB_VER_MAJOR = 0
SB_VER_MINOR = 0
SB_VER_YEAR = 0
SB_VER_MONTH = 0
SB_VER_DAY = 0

# IO Board Info (Get by UART)
IO_PROJECT_NAME = ''
IO_VER_MAJOR = 0
IO_VER_MINOR = 0
IO_VER_YEAR = 0
IO_VER_MONTH = 0
IO_VER_DAY = 0

### DEBUG ###

#FreePlay = True  # for Test Only, No Coin to Play 
FreePlay = False

#Mute = True  # for Test Only
Mute = False

InitWarningTimer = 5

#Need2InputPassword2CoinCountTableTimer = False  # for Test Only
Need2InputPassword2CoinCountTableTimer = True

#ScenarioTest_01Game = True  # for Test Only
ScenarioTest_01Game = False

#ScenarioTest_CountUp = True  # for Test Only
ScenarioTest_CountUp = False

#ScenarioTest_BigBull = True  # for Test Only
ScenarioTest_BigBull = False

#ScenarioTest_Cricket = True  # for Test Only
ScenarioTest_Cricket = False

EventDebugPrint_01Game = True  # Print Event Detail
#EventDebugPrint_01Game = False

EventDebugPrint_CountUp = True  # Print Event Detail
#EventDebugPrint_CountUp = False

EventDebugPrint_BigBull = True  # Print Event Detail
#EventDebugPrint_BigBull = False

EventDebugPrint_Cricket = True  # Print Event Detail
#EventDebugPrint_Cricket = False

EventDebugPrint_HappyAdd = True  # Print Event Detail
#EventDebugPrint_HappyAdd = False

#EnterIntoEngModeAtStartup = True  # for Test Only
EnterIntoEngModeAtStartup = False

#EnterIntoStatisticsAtStartup = True  # for Test Only
EnterIntoStatisticsAtStartup = False

#EnterIntoSettingMainMenuAtStartup = True  # for Test Only
EnterIntoSettingMainMenuAtStartup = False

#EnterIntoMachineTestAtStartup = True  # for Test Only
EnterIntoMachineTestAtStartup = False

#EnterIntoCoinCountTableAtStartup = True  # for Test Only
EnterIntoCoinCountTableAtStartup = False

#############

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

MSG_BOX_WIDTH = 700
MSG_BOX_HEIGHT = 350

ADC_CH_MAX = 32
ADC_CH_TTL = 26

EMPTY_FF = 0xFF
EMPTY_FFFF = 0xFFFF

KEY_EVENT4HALL_GUARD_TIMER = 0.1  # Second

IGNORE_ALL_EVENTS_UPON_ENTER_NEW_ROUND_TIMER = 1  # Seconds

TEXT_EFFECT_TIMER = 2  # Second
WINNER_SCREEN_TIMER = 3  # Second

INPUT_PASSWORD2SETTING_MAIN_MENU_TIMER = 10  # Seconds
INPUT_PASSWORD2COIN_COUNT_TABLE_TIMER = 10  # Seconds

SHOW_STATISTICS_TIMER = 10  # Second

PLAY_HALL_MUSIC_TIMER = 60  # Second

PCA9685_PWM_FREQUENCY = 100  # 50 ~ 12000, default 200

#KEY_POLLING = True

DELAY2CHECK_INTERNET_CONNECT = 0.1 # Second, for Test Only
#DELAY2CHECK_INTERNET_CONNECT = 5  # Second
CHECK_INTERNET_CONNECT_URL = "https://www.geeksforgeeks.org"
NTP_SERVER = "time.google.com"

UART_MSG_HANDLER_TIMER = 0.09  # Second

GIF_TIME_INV_MAIN_BACKGROUND =  0.01  # Second
SHOW_THROW_DARTS_TIMER = 1.5  #Second

GIF_TIME_INV_BULL = 0.08  # Second
GIF_TIME_INV_DBULL = 0.08  # Second
GIF_TIME_INV_DOUBLE = 0.05  # Second
GIF_TIME_INV_TRIPLE = 0.05  # Second
GIF_TIME_INV_BUST = 0.05  # Second
# --------------------------------------------------------------------
class ImgState(Enum):
	SELECT = 0  # Default
	UNSELECT = auto()
	DISABLE = auto()

class Pos():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Key(Enum):
    UP = 0
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    CENTER = auto()  # Blue
    ENTER = auto()   # Red
    AUDIT = auto()

    # --------------------------------------------
    COIN = auto()

    # --------------------------------------------
    DART_BACK = auto()
    DART_PASS = auto()
    DART_BACK2LAST_PLAYER = auto()

    # --------------------------------------------
    BLUE_HOLD_3_SEC = auto()
    BLUE_HOLD_10_SEC = auto()

    # --------------------------------------------
    PASSWORD_ENTER2SETTING_MAIN_MENU = auto()
    PASSWORD_ENTER2COIN_COUNT_TABLE = auto()
    
    PASSWORD_ENTER2SETTING_MAIN_MENU_NG = auto()
    PASSWORD_ENTER2COIN_COUNT_TABLE_NG = auto()

class Game(Enum):
    _01 = 0
    COUNTUP = auto()
    BIG_BULL = auto()
    CRICKET = auto()
    HAPPY_ADD = auto()
    MAX = auto()

class SubGame01(Enum):
    _301 = 0
    _501 = auto()
    _701 = auto()
    _901 = auto()
    _1501 = auto()
    MAX = auto()

class GetRtcDataCause(Enum):
    COIN_IN = auto()
    COIN_RETURN2ZERO = auto()
    AUDIT = auto()

tuplePlayerTextColor = ('#E62922', '#11F000', '#E89211', '#1D95D4')

tupleGame01OptionStr = ("Open", "Double", "Triple", "DT")

class Game01Option(Enum):
    OPEN = 0
    DOUBLE = auto()
    TRIPLE = auto()
    DT = auto()
    MAX = auto()

class Language(Enum):
    TRADITIONAL_CHINESE = 0
    ENGLISH = auto()
    MAX = auto()

class KeyEvent(Enum):
	PRESS = 0
	RELEASE = auto()
	HOLD1 = auto()            # The First Hold for HoldEvtType.FIRST, END or CONTINUOUS
	HOLD_CONTINUOUS = auto()  # Hold after the 1st one for HoldEvtType.CONTINUOUS

class KeyHoldEvtType(Enum):
	NONE = auto()        # No Hold Event
	FIRST = auto()       # Only the First Hold Event (Hold more than hold1_time_ms)
	END = auto()         # Only the End Hold Event
	CONTINUOUS = auto()

# BCM GPIO, Key, Debounce Time (ms) 兩次 event_detect 之間, 不包括第一次, 目前已無作用
#tupleKeyTbl = ( ( 6, Key.UP, 5 ), ( 19, Key.DOWN, 5 ), ( 26, Key.LEFT, 5 ), ( 16, Key.RIGHT, 5 ), ( 20, Key.CENTER, 5 ), ( 21, Key.ENTER, 5 ), ( 27, Key.COIN, 5 ) )
tupleKeyTbl = ( ( 0, Key.UP ), ( 0, Key.DOWN ), ( 0, Key.LEFT ), ( 0, Key.RIGHT ), ( 0, Key.CENTER ), ( 0, Key.ENTER ), ( 0, Key.AUDIT ) )

KEY_NUM_MAX = len(tupleKeyTbl)
