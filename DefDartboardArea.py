from enum import Enum, auto

BULL_SCORE = 25      # 紅心外圍 B, Outer Bull / Single Bull
BULLSEYE_SCORE = 50  # 紅心黑洞 B D, Inner Bull / Double Bull

class ID(Enum):
	MISS = 0

	# 數字單倍區 (外) : U
	SINGLE_U_1 = auto()   # 1
	SINGLE_U_2 = auto()   # 2
	SINGLE_U_3 = auto()   # 3
	SINGLE_U_4 = auto()   # 4
	SINGLE_U_5 = auto()   # 5
	SINGLE_U_6 = auto()   # 6
	SINGLE_U_7 = auto()   # 7
	SINGLE_U_8 = auto()   # 8
	SINGLE_U_9 = auto()   # 9
	SINGLE_U_10 = auto()  # 10
	SINGLE_U_11 = auto()  # 11
	SINGLE_U_12 = auto()  # 12
	SINGLE_U_13 = auto()  # 13
	SINGLE_U_14 = auto()  # 14
	SINGLE_U_15 = auto()  # 15
	SINGLE_U_16 = auto()  # 16
	SINGLE_U_17 = auto()  # 17
	SINGLE_U_18 = auto()  # 18
	SINGLE_U_19 = auto()  # 19
	SINGLE_U_20 = auto()  # 20

	# 數字單倍區 (內) : N
	SINGLE_N_1 = auto()   # 21
	SINGLE_N_2 = auto()   # 22
	SINGLE_N_3 = auto()   # 23
	SINGLE_N_4 = auto()   # 24
	SINGLE_N_5 = auto()   # 25
	SINGLE_N_6 = auto()   # 26
	SINGLE_N_7 = auto()   # 27
	SINGLE_N_8 = auto()   # 28
	SINGLE_N_9 = auto()   # 29
	SINGLE_N_10 = auto()  # 30
	SINGLE_N_11 = auto()  # 31
	SINGLE_N_12 = auto()  # 32
	SINGLE_N_13 = auto()  # 33
	SINGLE_N_14 = auto()  # 34
	SINGLE_N_15 = auto()  # 35
	SINGLE_N_16 = auto()  # 36
	SINGLE_N_17 = auto()  # 37
	SINGLE_N_18 = auto()  # 38
	SINGLE_N_19 = auto()  # 39
	SINGLE_N_20 = auto()  # 40

	# 數字雙倍區 : D
	DOUBLE_1 = auto()     # 41
	DOUBLE_2 = auto()     # 42
	DOUBLE_3 = auto()     # 43
	DOUBLE_4 = auto()     # 44
	DOUBLE_5 = auto()     # 45
	DOUBLE_6 = auto()     # 46
	DOUBLE_7 = auto()     # 47
	DOUBLE_8 = auto()     # 48
	DOUBLE_9 = auto()     # 49
	DOUBLE_10 = auto()    # 50
	DOUBLE_11 = auto()    # 51
	DOUBLE_12 = auto()    # 52
	DOUBLE_13 = auto()    # 53
	DOUBLE_14 = auto()    # 54
	DOUBLE_15 = auto()    # 55
	DOUBLE_16 = auto()    # 56
	DOUBLE_17 = auto()    # 57
	DOUBLE_18 = auto()    # 58
	DOUBLE_19 = auto()    # 59
	DOUBLE_20 = auto()    # 60

	# 數字三倍區 : T
	TRIPLE_1 = auto()     # 61
	TRIPLE_2 = auto()     # 62
	TRIPLE_3 = auto()     # 63
	TRIPLE_4 = auto()     # 64
	TRIPLE_5 = auto()     # 65
	TRIPLE_6 = auto()     # 66
	TRIPLE_7 = auto()     # 67
	TRIPLE_8 = auto()     # 68
	TRIPLE_9 = auto()     # 69
	TRIPLE_10 = auto()    # 70
	TRIPLE_11 = auto()    # 71
	TRIPLE_12 = auto()    # 72
	TRIPLE_13 = auto()    # 73
	TRIPLE_14 = auto()    # 74
	TRIPLE_15 = auto()    # 75
	TRIPLE_16 = auto()    # 76
	TRIPLE_17 = auto()    # 77
	TRIPLE_18 = auto()    # 78
	TRIPLE_19 = auto()    # 79
	TRIPLE_20 = auto()    # 80

	BULL = auto()         # 81, 紅心外圍 B, Outer Bull / Single Bull
	BULLSEYE = auto()     # 82, 紅心黑洞 B D, Inner Bull / Double Bull

	MAX = auto()          # 83, MAX

class AREA(Enum):
	NONE = 0
	SINGLE_OUTER = auto()   # 數字單倍區 (外) : U
	SINGLE_INNER = auto()   # 數字單倍區 (內) : N
	DOUBLE = auto()         # 數字雙倍區 : D
	TRIPLE = auto()         # 數字三倍區 : T
	#20230112
	TRIPLE15 = auto()       # 數字三倍區 : T15
	TRIPLE16 = auto()       # 數字三倍區 : T16
	TRIPLE17 = auto()       # 數字三倍區 : T17
	TRIPLE18 = auto()       # 數字三倍區 : T18
	TRIPLE19 = auto()       # 數字三倍區 : T19
	TRIPLE20 = auto()       # 數字三倍區 : T20
	#20230112
	BULL = auto()           # 紅心外圍 B, Outer Bull / Single Bull
	BULLSEYE = auto()       # 紅心黑洞 B D, Inner Bull / Double Bull

class MAGNIFY_RATIO(Enum):
	NONE = 0
	SINGLE = auto()
	DOUBLE = auto()
	TRIPLE = auto()
	#20230112
	TRIPLE15 = auto()       # 數字三倍區 : T15
	TRIPLE16 = auto()       # 數字三倍區 : T16
	TRIPLE17 = auto()       # 數字三倍區 : T17
	TRIPLE18 = auto()       # 數字三倍區 : T18
	TRIPLE19 = auto()       # 數字三倍區 : T19
	TRIPLE20 = auto()       # 數字三倍區 : T20
	#20230112
	
def Convert(id):
	area = AREA.NONE
	magnify_ratio = MAGNIFY_RATIO.NONE
	numeral_area_number = 0
	score = 0
    
	if id >= ID.SINGLE_U_1.value and id <= ID.SINGLE_U_20.value:
		area = AREA.SINGLE_OUTER
		magnify_ratio = MAGNIFY_RATIO.SINGLE
		numeral_area_number = id - ID.SINGLE_U_1.value + 1
		score = numeral_area_number
	elif id >= ID.SINGLE_N_1.value and id <= ID.SINGLE_N_20.value:
		area = AREA.SINGLE_INNER
		magnify_ratio = MAGNIFY_RATIO.SINGLE
		numeral_area_number = id - ID.SINGLE_N_1.value + 1
		score = numeral_area_number
	elif id >= ID.DOUBLE_1.value and id <= ID.DOUBLE_20.value:
		area = AREA.DOUBLE
		magnify_ratio = MAGNIFY_RATIO.DOUBLE
		numeral_area_number = id - ID.DOUBLE_1.value + 1
		score = numeral_area_number * 2
	#20230113
	elif id >= ID.TRIPLE_1.value and id <= ID.TRIPLE_14.value:
		area = AREA.TRIPLE
		magnify_ratio = MAGNIFY_RATIO.TRIPLE
		numeral_area_number = id - ID.TRIPLE_1.value + 1
		score = numeral_area_number * 3

	elif id == ID.TRIPLE_15.value:
		area = AREA.TRIPLE15
		magnify_ratio = MAGNIFY_RATIO.TRIPLE
		numeral_area_number = id - ID.TRIPLE_1.value + 1
		score = numeral_area_number * 3

	elif id == ID.TRIPLE_16.value:
		area = AREA.TRIPLE16
		magnify_ratio = MAGNIFY_RATIO.TRIPLE
		numeral_area_number = id - ID.TRIPLE_1.value + 1
		score = numeral_area_number * 3

	elif id == ID.TRIPLE_17.value:
		area = AREA.TRIPLE17
		magnify_ratio = MAGNIFY_RATIO.TRIPLE
		numeral_area_number = id - ID.TRIPLE_1.value + 1
		score = numeral_area_number * 3
	
	elif id == ID.TRIPLE_18.value:
		area = AREA.TRIPLE18
		magnify_ratio = MAGNIFY_RATIO.TRIPLE
		numeral_area_number = id - ID.TRIPLE_1.value + 1
		score = numeral_area_number * 3
	
	elif id == ID.TRIPLE_19.value:
		area = AREA.TRIPLE19
		magnify_ratio = MAGNIFY_RATIO.TRIPLE
		numeral_area_number = id - ID.TRIPLE_1.value + 1
		score = numeral_area_number * 3
	
	elif id == ID.TRIPLE_20.value:
		area = AREA.TRIPLE20
		magnify_ratio = MAGNIFY_RATIO.TRIPLE
		numeral_area_number = id - ID.TRIPLE_1.value + 1
		score = numeral_area_number * 3
	
	#2O23O113
	elif id == ID.BULL.value:
		area = AREA.BULL
		magnify_ratio = MAGNIFY_RATIO.SINGLE
		score = BULL_SCORE
	elif id == ID.BULLSEYE.value:
		area = AREA.BULLSEYE
		magnify_ratio = MAGNIFY_RATIO.DOUBLE
		score = BULLSEYE_SCORE
    
	return (area, magnify_ratio, numeral_area_number, score)

