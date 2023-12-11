from enum import Enum, auto
import threading
import pygame



class Effect(Enum):
	WINNER = 0
	MISS = auto()
	SINGLE = auto()
	DOUBLE = auto()
	TRIPLE = auto()
	BULL = auto()
	BULLSEYE = auto()
	BUST = auto()
	LOW_TON = auto()
	HIGH_TON = auto()
	HAT_TRICK = auto()
	TON_80 = auto()
	THREE_INNER_BULLS = auto()
	#THREE_IN_THE_BLACK = auto()
	OPEN_DOOR = auto()
	CLOSE_DOOR = auto()
	WHITE_HORSE = auto()
	TRIPLE_15 = auto()
	TRIPLE_16 = auto()
	TRIPLE_17 = auto()
	TRIPLE_18 = auto()
	TRIPLE_19 = auto()
	TRIPLE_20 = auto()


class Music(Enum):
	HALL = 0

class Key(Enum):
	KEY = 0
	BACK = auto()
	NEXT = auto()
	COIN = auto()
	
listFilePathNameEffect = [ "OGG/Winner.ogg", "OGG/Miss.ogg", "OGG/Single.ogg", "OGG/Double.ogg", "OGG/Triple.ogg", "OGG/Bull.ogg", "OGG/Bullseye.ogg", "OGG/Bust.ogg",
							"OGG/LowTon.ogg", "OGG/HighTon.ogg", "OGG/HatTrick.ogg", "OGG/Ton80.ogg", "OGG/ThreeInTheBlack.ogg", "OGG/OpenDoor.ogg", "OGG/CloseDoor.ogg", "OGG/WhiteHorse.ogg",
							 "OGG/Triple15.ogg", "OGG/Triple16.ogg", "OGG/Triple17.ogg", "OGG/Triple18.ogg", "OGG/Triple19.ogg", "OGG/Triple20.ogg"]

listFilePathNameMusic = [ "OGG/Hall.ogg" ]

listFilePathNameKey = [ "OGG/Key.ogg", "OGG/Back.ogg", "OGG/Next.ogg", "OGG/Coin.ogg" ]

class Channel(Enum):
	EFFECT = 0
	MUSIC = auto()
	KEY = auto()
	MAX = auto()

listChannelBusy = []

CHECK_CHANNEL_IDLE_TIME = 2  # Second
CheckChannelIdleTimer = None

def CheckChannelIdleTimeout():
	global listChannelBusy
	
	if not pygame.mixer.get_init():
		return

	for i in range(Channel.MAX.value):
		if not pygame.mixer.Channel(i).get_busy() and listChannelBusy[i]:
			listChannelBusy[i] = False  # Busy -> Idle
			if pygame.mixer.Channel(i).get_volume() != 0:
				pygame.mixer.Channel(i).set_volume(0)
				#print("Set mixer.ch[{}] Volume = 0".format(i))
	
	StartCheckChannelIdleTimer()

def StartCheckChannelIdleTimer():
	global CheckChannelIdleTimer
	
	CheckChannelIdleTimer = threading.Timer(CHECK_CHANNEL_IDLE_TIME, CheckChannelIdleTimeout)
	CheckChannelIdleTimer.start()

def SoundInit():
	global listChannelBusy

	for i in range(Channel.MAX.value):
		listChannelBusy.append(True)
	
	StartCheckChannelIdleTimer()

# 0 ~ 9 -> 0.1 ~ 1.0
def Volume2PygameMixerVol(ch):
	# _list = [ Setting.VolumeEffect, Setting.VolumeMusic, Setting.VolumeKey ]
	_list = [7, 7, 7]
	return (_list[ch] + 1) / 10

def ChannelRecoverVolume(ch):
	global listChannelBusy
	
	CheckChannelIdleTimer.cancel()
	
	listChannelBusy[ch] = True
	PygameMixerVol = Volume2PygameMixerVol(ch)
	if pygame.mixer.Channel(ch).get_volume() != PygameMixerVol:
		pygame.mixer.Channel(ch).set_volume(PygameMixerVol)
		#print("mixer.ch[{}] Recover Volume = {}".format(ch, PygameMixerVol))
	
	StartCheckChannelIdleTimer()

def PlayInfiniteHall():

	ChannelRecoverVolume(Channel.MUSIC.value)
	pygame.mixer.Channel(Channel.MUSIC.value).play(pygame.mixer.Sound(listFilePathNameMusic[Music.HALL.value]), -1)  # Play infinitely

'''
def PlayHallWithTimerMS(timerMS):
	if not CONST.Mute:
		Util.PRINT("PlayHall for {}ms".format(timerMS))
		Log2File.Write("PlayHall for {}ms".format(timerMS))
		ChannelRecoverVolume(Channel.MUSIC.value)
		pygame.mixer.Channel(Channel.MUSIC.value).play(pygame.mixer.Sound(listFilePathNameMusic[Music.HALL.value]), loops=-1, maxtime=timerMS)  # Play infinitely but Stop after a Timer
'''

def PlayHall():
	if not CONST.Mute:
		Util.PRINT("PlayHall")
		Log2File.Write("PlayHall")
		ChannelRecoverVolume(Channel.MUSIC.value)
		pygame.mixer.Channel(Channel.MUSIC.value).play(pygame.mixer.Sound(listFilePathNameMusic[Music.HALL.value]))

def StopHall():
	Util.PRINT("StopHall")
	Log2File.Write("StopHall")
	pygame.mixer.Channel(Channel.MUSIC.value).stop()

'''
def IsMusicChannelBusy():
	return pygame.mixer.Channel(Channel.MUSIC.value).get_busy()
'''

# Press Key ------------------------------------------------------------------------------
def PlayKey():
	if not CONST.Mute:
		ChannelRecoverVolume(Channel.KEY.value)
		pygame.mixer.Channel(Channel.KEY.value).play(pygame.mixer.Sound(listFilePathNameKey[Key.KEY.value]))

def PlayBack():
	if not CONST.Mute:
		ChannelRecoverVolume(Channel.KEY.value)
		pygame.mixer.Channel(Channel.KEY.value).play(pygame.mixer.Sound(listFilePathNameKey[Key.BACK.value]))

def PlayNext():
	if not CONST.Mute:
		ChannelRecoverVolume(Channel.KEY.value)
		pygame.mixer.Channel(Channel.KEY.value).play(pygame.mixer.Sound(listFilePathNameKey[Key.NEXT.value]))

def PlayCoin():
	if not CONST.Mute:
		ChannelRecoverVolume(Channel.KEY.value)
		pygame.mixer.Channel(Channel.KEY.value).play(pygame.mixer.Sound(listFilePathNameKey[Key.COIN.value]))

# Effect ----------------------------------------------------------------------------------
def PlayEffect(effectEnum):
	if effectEnum is not None and not CONST.Mute:
		ChannelRecoverVolume(Channel.EFFECT.value)
		pygame.mixer.Channel(Channel.EFFECT.value).play(pygame.mixer.Sound(listFilePathNameEffect[effectEnum.value]))
	
def StopEffect():
	pygame.mixer.Channel(Channel.EFFECT.value).stop()

# ----------------------------------------------------------------------------------------
def StopAll():
	pygame.mixer.stop()
	pygame.mixer.quit()

# ----------------------------------------------------------------------------------------
def PlayVolumeAdjust(vol):
	global listChannelBusy
	
	if not CONST.Mute:
		CheckChannelIdleTimer.cancel()

		ch = Channel.KEY.value
		listChannelBusy[ch] = True

		PygameMixerVol = (vol + 1) / 10  # 0 ~ 9 -> 0.1 ~ 1.0

		if pygame.mixer.Channel(ch).get_volume() != PygameMixerVol:
			pygame.mixer.Channel(ch).set_volume(PygameMixerVol)
			#print("mixer.ch[{}] Recover Volume = {}".format(ch, PygameMixerVol))

		StartCheckChannelIdleTimer()

		pygame.mixer.Channel(Channel.KEY.value).play(pygame.mixer.Sound(listFilePathNameKey[Key.NEXT.value]))
