from enum import Enum, auto
import logging
import os
from datetime import datetime

from pathlib import Path
from shutil import rmtree

import CONST
import Setting

# DEBUG < INFO < WARNING < ERROR / EXCEPTION < CRITICAL
# Don't Use DEBUG, because it already be used by other modules
class Level(Enum):  # Log Level
	INFO = auto()
	WARNING = auto()
	ERROR = auto()
	CRITICAL = auto()

RootDir = "Log"
TodayDir = ""
CurFilePathName = ""
TempFilePathName = ""

Year = ""
Month = ""
Day = ""
Hour = ""
Minute = ""
Second = ""

AlreadyMakeTodayDir = False
AlreadySetLoggingBasicConfig = False

def Init():
	global TodayDir, CurFilePathName, TempFilePathName, Year, Month, Day, Hour, Minute, Second

	if not os.path.exists(RootDir):
		os.makedirs(RootDir)

	CurDateTime = datetime.now()
	Year = str(CurDateTime.year)
	Month = "{:02d}".format(CurDateTime.month)
	Day = "{:02d}".format(CurDateTime.day)
	Hour = "{:02d}".format(CurDateTime.hour)
	Minute = "{:02d}".format(CurDateTime.minute)
	Second = "{:02d}".format(CurDateTime.second)
	
	TodayDir = RootDir + '/' + Year + '/' + Month + '/' + Day
	CurFilePathName = TodayDir + '/' + Year + Month + Day + '-' + Hour + Minute + Second + '.log'
	TempFilePathName = 'Temp/' + Year + Month + Day + '-' + Hour + Minute + Second + '.log'
	
	#print('Log2File: CurFilePathName', CurFilePathName)
	#print('Log2File: TempFilePathName', TempFilePathName)

def MakeTodayDir():
	global AlreadyMakeTodayDir
	
	if not AlreadyMakeTodayDir:
		AlreadyMakeTodayDir = True
		if not os.path.exists(TodayDir):
			os.makedirs(TodayDir)

def SetLoggingBasicConfig():
	global AlreadySetLoggingBasicConfig
	
	if not AlreadySetLoggingBasicConfig:
		AlreadySetLoggingBasicConfig = True
		#logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s >> %(message)s", filename=CurFilePathName, filemode='w')
		logging.basicConfig(level=logging.INFO, format="%(levelname)1.1s %(asctime)s.%(msecs)03d >> %(message)s", filename=CurFilePathName, filemode='w', datefmt='%H:%M:%S')

def Write(string, enumLevel=Level.INFO):
	if Setting.Log2FileEnable == 1:
		MakeTodayDir()
		SetLoggingBasicConfig()

		if enumLevel == Level.INFO:
			logging.info(string)
		elif enumLevel == Level.WARNING:
			logging.warning(string)
		elif enumLevel == Level.ERROR:
			logging.error(string)
		elif enumLevel == Level.CRITICAL:
			logging.critical(string)

def ClearAll():
	print("Clear All Log Files")
	os.rename(CurFilePathName, TempFilePathName)

	for path in Path(RootDir).glob("**/*"):
		if path.is_file():
			path.unlink()
		elif path.is_dir():
			rmtree(path)

	os.makedirs(TodayDir)
	os.rename(TempFilePathName, CurFilePathName)
