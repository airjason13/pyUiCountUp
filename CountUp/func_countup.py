from .global_def import *
from enum import Enum, auto
import DefDartboardArea as DBA
import Setting as Setting
# from .ui_countup_main import UiCountUp

class Event(Enum):
    NORMAL = 0
    NO_MORE_DART = auto()
    MISS = auto()
    NEXT_PLAYER = auto()
    NEXT_ROUND = auto()
    GAME_OVER = auto()
    NO_DART2BYPASS_BY_PASSS_KEY = auto()
    BYPASS_DART_BY_PASS_KEY = auto()
    NO_DART2RECOVER_BY_BACK_KEY = auto()
    RECOVER_DART_BY_BACK_KEY = auto()
    ROUND_END_SPECIAL_SCORE = auto()
    NO_MORE_BACK_DART = auto()
    BACK2LAST_PLAYER_BY_HOLD_BACK_KEY = auto()  # 返回上一個 Player, 因可能鏢掉下剛好敲到 ENTER/NEXT Key (CurDart = 0 and not the first Round/Player)


class RoundEndSpecialScore(Enum): # 射完第三鏢後，特殊效果
    NONE = 0
    LOW_TON = auto()                 # 單一回合三鏢達到 100 ~ 150 分
    HIGH_TON = auto()                # 單一回合三鏢達到 151 以上
    TON_80 = auto()                  # 單一回合三鏢皆命中 20 分三倍區
    HAT_TRICK = auto()               # 單一回合三鏢皆命中外黑心
    THREE_INNER_BULLS = auto()       # 單一回合三鏢皆命中內紅心
    # #THREE_IN_A_BED = auto()         # 單一回合三鏢皆命中相同數字分三倍區
    # #THREE_IN_THE_BLACK = auto()     # 單一回合三鏢皆命中外黑心


class GameStatistics(Enum):         # 遊戲結束後的統計資料
    DART_AVG_SCORE = 0                # 每鏢平均得分
    ROUND_AVG_SCORE = auto()          # 每局平均得分
    TON_80_TIMES = auto()             # 總次數:單一回合三鏢皆命中 20 分三倍區
    HIGH_TON_TIMES = auto()           # 總次數:單一回合三鏢達到 151 以上
    LOW_TON_TIMES = auto()            # 總次數:單一回合三鏢達到 100 ~ 150 分
    THREE_INNER_BULLS_TIMES = auto()  # 總次數:單一回合三鏢皆命中內紅心
    HAT_TRICK_TIMES = auto()          # 總次數:單一回合三鏢皆命中外黑心
    THREE_IN_A_BED_TIMES = auto()     # 總次數:單一回合三鏢皆命中相同數字分三倍區
    MAX = auto()

# BYPASS_ALL_MISS_BY_NEXT_KEY = auto()
# ROUND_END_BY_NEXT_KEY = auto()


class FuncCountUp:

    ROUND_MAX = 8
    PLAYER_MAX = 4
    DART_MAX_EACH_ROUND = 3

    LOW_TON_SCORE_MIN = 100
    LOW_TON_SCORE_MAX = 150
    HIGH_TON_SCORE_MIN = 151

    def __init__(self, _game_ui, _ui_round_info, _ui_player_info,
                 round_max=ROUND_MAX, player_max=PLAYER_MAX, dart_max_each_round=DART_MAX_EACH_ROUND):

        self.game_ui = _game_ui
        self.ui_round_info = _ui_round_info
        self.ui_round_info = _ui_player_info
        self.is_game_over = False

        self.can_back_2_last_player = False
        self.event_callback = self.game_ui.ui_callback
        self.player_max = player_max
        self.round_max = round_max

        self.list_cur_score = [0] * self.player_max
        self.list_darts = []
        self.current_round = 0
        self.current_player = 0
        self.current_dart = 0
        self.list_back_dart = []
        self.list_game_statistics = []
        self.list_winners = [False] * self.player_max

        self.list_darts = [[[Dart() for i in range(self.DART_MAX_EACH_ROUND)] for j in range(self.PLAYER_MAX)] for k in range(self.ROUND_MAX)]

        self.list_game_statistics.clear()
        self.list_game_statistics = [[0 for i in range(GameStatistics.MAX.value)] for j in range(self.player_max)]

        self.list_back_dart.clear()
        self.list_back_dart = [ 0 for i in range(self.player_max)]

    def round_or_player_change(self):  # or Gameover
        # global CurRound, CurPlayer, CurDart, GameOver, CanBack2LastPlayer

        self.current_player += 1  # Next Player
        _curDart = self.current_dart
        self.current_dart = 0
        if self.current_player == self.player_max:  # Next Round
            self.current_round += 1
            if self.current_round == self.round_max:  # Normal Game Over
                self.is_game_over = True
                self.judge_winner() # JudgeWinner()
                self.event_callback(Event.GAME_OVER, Player=self.player_max - 1, Dart=_curDart, Winner=self.list_winners,
                              listTtlScore=self.list_cur_score)
            else:
                self.CurPlayer = 0
                self.event_callback(Event.NEXT_ROUND, Round=self.current_round, Player=self.current_player,
                                    TtlScore=self.list_cur_score[self.current_player])
        else:
            self.event_callback(Event.NEXT_PLAYER, Round=self.current_round, Player=self.current_player,
                                TtlScore=self.list_cur_score[self.current_player])
        if not self.is_game_over:
            self.can_back_2_last_player = True

    def got_nex_key_event(self):
        if not self.is_game_over:
            if self.current_dart == self.DART_MAX_EACH_ROUND:
                self.round_or_player_change()
            else:
                for i in range(self.current_dart, self.DART_MAX_EACH_ROUND):
                    self.list_darts[self.current_round][self.current_player][i].Bypass_AllMissByNext = True

    def got_back_key_event(self):  # Dart: 0  第一鏢 -> 1  第二鏢 -> 2  第三鏢 -> 3
        # global CurDart, listDarts, listCurScore, GameOver, listBackDartTtl  # , RoundEndByNextKey

        if not self.is_game_over:
            if self.current_dart == 0:
                self.event_callback(Event.NO_DART2RECOVER_BY_BACK_KEY)
            elif self.list_back_dart[self.current_player] == Setting.DartReturnTimes:
                self.event_callback(Event.NO_MORE_BACK_DART, Round=self.current_round, Player=self.current_player,
                                    Dart=self.current_dart)
            else:
                self.list_back_dart[self.current_player] += 1
                print("Player {}, BackDartTtl {}".format(self.current_player + 1, self.list_back_dart[self.current_player]))
                # RoundEndByNextKey = False
                if (self.current_dart == self.DART_MAX_EACH_ROUND
                        and self.list_darts[self.current_round][self.current_player][self.DART_MAX_EACH_ROUND - 1].Bypass_AllMissByNext):  # 應該不會再遇到, 因為 Next 會直接 Player/Round Change
                    self.current_dart = 0
                    for i in range(0, self.DART_MAX_EACH_ROUND):
                        dart = self.list_darts[self.current_round][self.current_player][i]
                        if dart.Bypass_AllMissByNext:
                            dart.Clear()
                        else:
                            CurDart = i + 1
                    self.event_callback(Event.RECOVER_DART_BY_BACK_KEY, Round=self.current_round,
                                        Player=self.current_player, Dart=self.current_dart,
                                        TtlScore=self.list_cur_score[self.current_player])
                else:
                    self.current_dart -= 1
                    dart = self.list_darts[self.current_round][self.current_player][self.current_dart]
                    self.list_cur_score[self.current_player] = dart.TtlScoreBeforeCountThisDart
                    dart.Clear()
                    self.event_callback(Event.RECOVER_DART_BY_BACK_KEY, Round=self.current_round,
                                        Player=self.current_player, Dart=self.current_dart,
                                        TtlScore=self.list_cur_score[self.current_player])

    def got_pass_key_event(self):  # Bypass this Dart
        # global CurDart, CanBack2LastPlayer

        if not self.is_game_over:
            if self.current_dart < self.DART_MAX_EACH_ROUND:
                dart = self.list_darts[self.current_round][self.current_player][self.current_dart]
                dart.TtlScoreBeforeCountThisDart = self.list_cur_score[self.current_player]
                CanBack2LastPlayer = False
                if self.is_to_the_end_of_game(True):
                    self.judge_winner()
                    self.event_callback(Event.BYPASS_DART_BY_PASS_KEY, Round=self.current_round,
                                        Player=self.current_player, Dart=self.current_dart, Winner=self.list_winners)
                else:
                    self.event_callback(Event.BYPASS_DART_BY_PASS_KEY, Round=self.current_round,
                                        Player=self.current_player, Dart=self.current_dart)
                self.current_dart += 1
            else:
                self.event_callback(Event.NO_DART2BYPASS_BY_PASSS_KEY)

    def got_back_2_last_player_by_hold_back_key_event(self):  # Return to the Last Player/Round
        # global CurRound, CurPlayer, CurDart, listBackDartTtl, CanBack2LastPlayer

        if not self.is_game_over:
            LastPlayer = self.current_player
            if self.player_max > 1:
                if self.current_player == 0:
                    LastPlayer = self.player_max - 1
                else:
                    LastPlayer = self.current_player - 1

            if self.can_back_2_last_player and self.list_back_dart[LastPlayer] < Setting.DartReturnTimes:
                self.can_back_2_last_player = False
                self.list_back_dart[LastPlayer] += 1
                print("Player {}, BackDartTtl {}".format(LastPlayer + 1, self.list_back_dart[LastPlayer]))

                CurPlayer = LastPlayer
                if self.player_max == 1 or self.current_player == self.player_max - 1:
                    self.current_round -= 1

                self.current_dart = self.DART_MAX_EACH_ROUND
                for i in range(self.DART_MAX_EACH_ROUND - 1, -1, -1):  # 2, 1, 0
                    dart = self.list_darts[self.current_round][self.current_player][i]
                    if dart.Bypass_AllMissByNext:
                        dart.Clear()
                        self.current_dart -= 1
                    else:
                        break;

                self.event_callback(Event.BACK2LAST_PLAYER_BY_HOLD_BACK_KEY, Round=self.current_round,
                                        Player=self.current_player, Dart=self.current_dart,
                              TtlScore=self.list_cur_score[self.current_player])
            else:
                self.event_callback(Event.NO_DART2RECOVER_BY_BACK_KEY)

    def got_shoot_dart_event(self, dba_id):
        log.debug("")
        if not self.is_game_over:
            self.event_callback(Event.NO_MORE_DART)
        else:
            # dart = self.list_darts[CurRound][CurPlayer][CurDart]
            dart = self.list_darts[self.current_round][self.current_player][self.current_dart]
            dart.GotDbaId(dba_id)
            dart.TtlScoreBeforeCountThisDart = self.list_cur_score[self.current_player]
            CanBack2LastPlayer = False
            event = Event.NORMAL

            if dart.Miss:
                event = Event.MISS
            else:
                self.list_cur_score[self.current_player] += dart.Score

            if event == Event.MISS:
                if self.is_to_the_end_of_game(True):
                    self.judge_winner()
                    self.event_callback(event, Round=self.current_round, Player=self.current_player,
                                        Dart=self.current_dart, Winner=self.list_winners)
                else:
                    self.event_callback(event, Round=self.current_round, Player=self.current_player,
                                        Dart=self.current_dart)
            else:
                _RoundEndSpecialScore = RoundEndSpecialScore.NONE
                if self.current_dart == (self.DART_MAX_EACH_ROUND - 1):
                    if self.Is_HAT_TRICK(self.current_round, self.current_player):
                        _RoundEndSpecialScore = RoundEndSpecialScore.HAT_TRICK
                    elif self.Is_THREE_INNER_BULLS(self.current_round, self.current_player):
                        _RoundEndSpecialScore = RoundEndSpecialScore.THREE_INNER_BULLS
                    # elif Is_THREE_IN_THE_BLACK(CurRound, CurPlayer):
                    #	_RoundEndSpecialScore = RoundEndSpecialScore.THREE_IN_THE_BLACK
                    elif self.Is_TON_80(self.current_round, self.current_player):
                        _RoundEndSpecialScore = RoundEndSpecialScore.TON_80
                    # elif Is_THREE_IN_A_BED(CurRound, CurPlayer):
                    #	_RoundEndSpecialScore = RoundEndSpecialScore.THREE_IN_A_BED
                    elif self.Is_LOW_TON(self.current_round, self.current_player):
                        _RoundEndSpecialScore = RoundEndSpecialScore.LOW_TON
                    elif self.Is_HIGH_TON(self.current_round, self.current_player):
                        _RoundEndSpecialScore = RoundEndSpecialScore.HIGH_TON

                if _RoundEndSpecialScore == RoundEndSpecialScore.NONE:
                    if self.is_to_the_end_of_game(True):
                        self.judge_winner()
                        self.event_callback(event, Round=self.current_round, Player=self.current_player,
                                            Dart=self.current_dart, Score=dart.Score,
                                            TtlScore=self.list_cur_score[self.current_player], Enum_DBA_Area=dart.EnumArea,
                                            Enum_DBA_MagnifyRatio=dart.EnumMagnifyRatio,
                                            NumeralAreaNumber=dart.NumeralAreaNumber, Winner=self.list_winners)
                    else:
                        self.event_callback(event, Round=self.current_round, Player=self.current_player,
                                            Dart=self.current_dart, Score=dart.Score,
                                            TtlScore=self.list_cur_score[self.current_player], Enum_DBA_Area=dart.EnumArea,
                                            Enum_DBA_MagnifyRatio=dart.EnumMagnifyRatio,
                                            NumeralAreaNumber=dart.NumeralAreaNumber)
                else:
                    if self.is_to_the_end_of_game(True):
                        self.judge_winner()
                        self.event_callback(Event.ROUND_END_SPECIAL_SCORE, Round=self.current_round,
                                            Player=self.current_player, Dart=self.current_dart,
                                            Score=dart.Score, TtlScore=self.list_cur_score[self.current_player],
                                            Enum_DBA_Area=dart.EnumArea,
                                            Enum_DBA_MagnifyRatio=dart.EnumMagnifyRatio,
                                            NumeralAreaNumber=dart.NumeralAreaNumber,
                                            Enum_RoundEndSpecialScore=_RoundEndSpecialScore, Winner=self.list_winners)
                    else:
                        self.event_callback(Event.ROUND_END_SPECIAL_SCORE, Round=self.current_round,
                                            Player=self.current_player, Dart=self.current_dart,
                                            Score=dart.Score, TtlScore=self.list_cur_score[self.current_player],
                                            Enum_DBA_Area=dart.EnumArea,
                                            Enum_DBA_MagnifyRatio=dart.EnumMagnifyRatio,
                                            NumeralAreaNumber=dart.NumeralAreaNumber,
                                            Enum_RoundEndSpecialScore=_RoundEndSpecialScore)

            self.current_dart += 1 #CurDart += 1

    def Is_LOW_TON(self, _round, _player):  # 單一回合三鏢達到 100 ~ 150 分
        ttlScore = 0
        for i in range(0, self.DART_MAX_EACH_ROUND):
            ttlScore += self.list_darts[_round][_player][i].Score
        if ttlScore >= self.LOW_TON_SCORE_MIN and ttlScore <= self.LOW_TON_SCORE_MAX:
            return True
        else:
            return False

    def Is_HIGH_TON(self, _round, _player):  # 單一回合三鏢達到 151 以上
        ttlScore = 0
        for i in range(0, self.DART_MAX_EACH_ROUND):
            ttlScore += self.list_darts[_round][_player][i].Score
        if ttlScore >= self.HIGH_TON_SCORE_MIN:
            return True
        else:
            return False

    def Is_HAT_TRICK(self, _round, _player):  # 單一回合三鏢皆命中外黑心
        allBULL = True
        for i in range(0, self.DART_MAX_EACH_ROUND):
            if self.list_darts[_round][_player][i].DbaId != DBA.ID.BULL.value:
                allBULL = False
                break
        return allBULL

    def Is_THREE_INNER_BULLS(self, _round, _player):  # 單一回合三鏢皆命中內紅心
        allBULLSEYE = True
        for i in range(0, self.DART_MAX_EACH_ROUND):
            if self.list_darts[_round][_player][i].DbaId != DBA.ID.BULLSEYE.value:
                allBULLSEYE = False
                break
        return allBULLSEYE

    def Is_TON_80(self, _round, _player):  # 單一回合三鏢皆命中 20 分三倍區
        allTRIPLE_20 = True
        for i in range(0, self.DART_MAX_EACH_ROUND):
            if self.list_darts[_round][_player][i].DbaId != DBA.ID.TRIPLE_20.value:
                allTRIPLE_20 = False
                break
        return allTRIPLE_20

    def Is_THREE_IN_A_BED(self, _round, _player):  # 單一回合三鏢皆命中相同數字分三倍區
        allTRIPLE_SameNumeralAreaNumber = True
        NumeralAreaNumber = 0
        for i in range(0, self.DART_MAX_EACH_ROUND):
            dart = self.list_darts[_round][_player][i]
            if dart.EnumMagnifyRatio != DBA.MAGNIFY_RATIO.TRIPLE:
                allTRIPLE_SameNumeralAreaNumber = False
                break
            else:
                if NumeralAreaNumber == 0:
                    NumeralAreaNumber = dart.NumeralAreaNumber
                else:
                    if NumeralAreaNumber != dart.NumeralAreaNumber:
                        allTRIPLE_SameNumeralAreaNumber = False
                        break
        return allTRIPLE_SameNumeralAreaNumber

    def is_to_the_end_of_game(self, check_cur_dart): #.checkCurDart):
        result = False
        if self.ui_round_info.round_num_current == self.round_max \
                and self.ui_player_info.current_player == (self.player_max - 1):
            result = True
        if result is True and check_cur_dart:
            if self.ui_player_info.darts.current_dart < (self.DART_MAX_EACH_ROUND -1):
                result = False
        return result

    def judge_winner(self):
        # global listWinner

        _listTtlScore = [0] * self.player_max
        for i in range(self.player_max):
            _listTtlScore[i] = self.list_cur_score[i] #listCurScore[i]
        WinnerScore = max(_listTtlScore)
        for i in range(self.player_max):
            self.list_winners = True if _listTtlScore[i] == WinnerScore else False
            # listWinner[i] = True if _listTtlScore[i] == WinnerScore else False

class GameStatistics(Enum):         # 遊戲結束後的統計資料
    DART_AVG_SCORE = 0                # 每鏢平均得分
    ROUND_AVG_SCORE = auto()          # 每局平均得分
    TON_80_TIMES = auto()             # 總次數:單一回合三鏢皆命中 20 分三倍區
    HIGH_TON_TIMES = auto()           # 總次數:單一回合三鏢達到 151 以上
    LOW_TON_TIMES = auto()            # 總次數:單一回合三鏢達到 100 ~ 150 分
    THREE_INNER_BULLS_TIMES = auto()  # 總次數:單一回合三鏢皆命中內紅心
    HAT_TRICK_TIMES = auto()          # 總次數:單一回合三鏢皆命中外黑心
    THREE_IN_A_BED_TIMES = auto()     # 總次數:單一回合三鏢皆命中相同數字分三倍區
    MAX = auto()


class Dart:
    def clear(self):
        self.DbaId = 0
        self.EnumArea = DBA.AREA.NONE
        self.EnumMagnifyRatio = DBA.MAGNIFY_RATIO.NONE
        self.NumeralAreaNumber = 0
        self.Score = 0

        self.Miss = False

        self.Bypass_AllMissByNext = False

        self.TtlScoreBeforeCountThisDart = 0

    def __init__(self):
        self.clear()
        self.DbaId = 0
        self.EnumArea = DBA.AREA.NONE
        self.EnumMagnifyRatio = DBA.MAGNIFY_RATIO.NONE
        self.NumeralAreaNumber = 0
        self.Score = 0

        self.Miss = False

        self.Bypass_AllMissByNext = False

        self.TtlScoreBeforeCountThisDart = 0

    def got_dba_id(self, id):
        self.DbaId = id
        (self.EnumArea, self.EnumMagnifyRatio, self.NumeralAreaNumber, self.Score) = DBA.Convert(id)

        if self.EnumArea == DBA.AREA.NONE:
            self.Miss = True

