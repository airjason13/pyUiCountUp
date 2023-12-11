import os
from datetime import datetime
from PIL import Image

import requests
import ntplib
import time

import Setting
import CONST
import Log2File

import platform


def PRINT(string):
	if Setting.LogEnable == 1:
		print(string)

def PRINT_NoLF(string):
	if Setting.LogEnable == 1:
		print(string, end='')

def PRINT_LF():
	if Setting.LogEnable == 1:
		print()

def GetWeekdayStr(weekdayVal, abbreviation):
	s = ''
	if weekdayVal == 0:
		if abbreviation:
			s = 'Sun'
		else:
			s = 'Sunday'
	elif weekdayVal == 1:
		if abbreviation:
			s = 'Mon'
		else:
			s = 'Monday'
	elif weekdayVal == 2:
		if abbreviation:
			s = 'Tue'
		else:
			s = 'Tuesday'
	elif weekdayVal == 3:
		if abbreviation:
			s = 'Wed'
		else:
			s = 'Wednesday'
	elif weekdayVal == 4:
		if abbreviation:
			s = 'Thu'
		else:
			s = 'Thursday'
	elif weekdayVal == 5:
		if abbreviation:
			s = 'Fri'
		else:
			s = 'Friday'
	elif weekdayVal == 6:
		if abbreviation:
			s = 'Sat'
		else:
			s = 'Saturday'
	return s

def PrintCurDateTime():
	CurDateTime = datetime.now()
	#print('Weekday', CurDateTime.weekday())  週一的索引為 0，週日為 6
	w = CurDateTime.weekday()
	if w == 0:
		w = 1
	elif w == 6:
		w = 0
	else:
		w += 1		
	WeekStr = GetWeekdayStr(w, False)
	Str = "{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}, {}".format(CurDateTime.year, CurDateTime.month, CurDateTime.day, CurDateTime.hour, CurDateTime.minute, CurDateTime.second, WeekStr)
	print(Str)

def UartRtcData2Str(listRtcData, startListIdx, addYear2000, includeSecond, includeWeekday):
	i = startListIdx
	s = ''
	if addYear2000:
		s = '20'
	s += "{:02d}-{:02d}-{:02d} {:02d}:{:02d}".format(listRtcData[i]&0x7F, listRtcData[i+1]&0x7F, listRtcData[i+2]&0x7F, listRtcData[i+3]&0x7F, listRtcData[i+4]&0x7F)
	if includeSecond:
		s += ":{:02d}".format(listRtcData[i+5]&0x7F)
	if includeWeekday:
		s += (' ' + GetWeekdayStr(listRtcData[i+6]&0x7F, True))
	return s    

# "21-11-15 18:09" -> [ 21, 11, 15, 18, 9 ]
def DateTimeToMinuteStr2UartIntList(strDateTimeToMinute):
	if strDateTimeToMinute is None or strDateTimeToMinute =='':
		return [ 0x80, 0x80, 0x80, 0x80, 0x80 ]
	
	listDT = strDateTimeToMinute.split(' ')  # [ '21-11-15', '18:09' ]
	listD = listDT[0].split('-')  # [ '21', '11', '15' ]
	listT = listDT[1].split(':')  # [ '18', '09' ]
	_list = []
	for i in range(3):
		_list.append(0x80 + int(listD[i]))
	for i in range(2):
		_list.append(0x80 + int(listT[i]))
	return _list

# "21-11-15 18:09:58" + weekday -> [ 21, 11, 15, 18, 9, 58, weekday ]
# Year can be +2000
def DateTimeToSecondStr2UartIntList(strDateTimeToSecond, weekday):
	listDT = strDateTimeToSecond.split(' ')  # [ '21-11-15', '18:09:58' ]
	listD = listDT[0].split('-')  # [ '21', '11', '15' ]
	if int(listD[0]) >= 2000:
		listD[0] = str(int(listD[0])-2000)
	listT = listDT[1].split(':')  # [ '18', '09', '58' ]
	_list = []
	for i in range(3):
		_list.append(0x80 + int(listD[i]))
	for i in range(3):
		_list.append(0x80 + int(listT[i]))
	_list.append(0x80 + weekday)
	return _list

# sudo date -s '2022-12-25 12:34:56'
def SetSystemDateTime(YearNo2000, Month, Day, Hour, Minute, Second):
	if YearNo2000 >= 22:  # for safety
		s = "'{}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'".format(YearNo2000+2000, Month, Day, Hour, Minute, Second)
		os.system("sudo date -s " + s)
		PRINT("Set System DateTime " + s)
		Log2File.Write("Set System DateTime " + s)
	#PrintCurDateTime()

def GetKeyTableIdxByBcmPin(bcm_pin):  # return -1 if not found
	for i in range(CONST.KEY_NUM_MAX):
		if(bcm_pin == CONST.tupleKeyTbl[i][0]):
			return i
	return -1

def GetKeyTableIdxByEnumKey(enumKey):  # return -1 if not found
	for i in range(CONST.KEY_NUM_MAX):
		if(enumKey == CONST.tupleKeyTbl[i][1]):
			return i
	return -1

def DisableNTP():
	os.system('sudo timedatectl set-ntp false')

def CheckInternetConnection():
	url = CONST.CHECK_INTERNET_CONNECT_URL
	timeout = 10
	try:
		# requesting URL
		request = requests.get(url, timeout=timeout)
		#PRINT("Internet is on")
		return True
	  
	# catching exception
	#except (requests.ConnectionError, requests.Timeout) as exception:
	#	PRINT("Internet is off")
	except Exception as ex:
		s = 'Internet Connect Error: {}'.format(ex)
		PRINT(s)
		Log2File.Write(s)
	
	return False

# return '2022-12-25 12:34:56 w' if OK
# return '' if NG
def GetNtpDateTime(alsoSetSysDateTime):
	url = CONST.NTP_SERVER
	c = ntplib.NTPClient()
	try:
		response = c.request(url)
		ts = response.tx_time
		_date = time.strftime('%Y-%m-%d',time.localtime(ts))
		_time = time.strftime('%X',time.localtime(ts))
		_weekday = time.strftime('%w',time.localtime(ts))  # 0 ~ 6, from Sunday
		s = "NTP {} {} w{}".format(_date, _time, _weekday)
		PRINT(s)
		Log2File.Write(s)
		
		if alsoSetSysDateTime:
			s = "'{} {}'".format(_date, _time)
			os.system("sudo date -s " + s)
			PRINT("Set System DateTime " + s)
			Log2File.Write("Set System DateTime " + s)
		return "{} {} {}".format(_date, _time, _weekday)

	except Exception as ex:
		s = 'NTP Client Request Error: {}'.format(ex)
		PRINT(s)
		Log2File.Write(s)

	return ''

# volume: 0~9
def GetCvlcCmdStr(volume, filepathname):
    try:
        if '64bit' in platform.architecture():
            s = "ffplay -fs -autoexit " + filepathname
        else:
	        sGain = (volume + 1) / 10
	        s = "cvlc -f --video-on-top --no-video-title-show --play-and-exit --gain={} {}".format(sGain, filepathname)
	        #print("GetCvlcCmdStr vol {}, file {}, gain {}".format(volume, filepathname, sGain))
	        #print(s)

    except Exception as e:
        Log2File.Write(e)
    return s

def GetFilesTtlInDir(sDir):
	cnt = 0
	for path in os.scandir(sDir):
		if path.is_file():
			cnt += 1
	return cnt

def GetGifFilePathNameList_Bull(listFilePathName):
	if listFilePathName != []:
		listFilePathName.clear()
	fileTtl = GetFilesTtlInDir('Image/GIF/BULL')
	if fileTtl > 0:
		for i in range(fileTtl):
			listFilePathName.append("Image/GIF/BULL/Triple_L_Effects_-{:02d}.png".format(i))
	return fileTtl

def GetGifFilePathNameList_DBull(listFilePathName):
	if listFilePathName != []:
		listFilePathName.clear()
	fileTtl = GetFilesTtlInDir('Image/GIF/DBULL')
	if fileTtl > 0:
		for i in range(fileTtl):
			listFilePathName.append("Image/GIF/DBULL/Triple_L_Effects_-{:02d}.png".format(i))
	return fileTtl

def GetGifFilePathNameList_DOUBLE(listFilePathName):
	if listFilePathName != []:
		listFilePathName.clear()
	fileTtl = GetFilesTtlInDir('Image/GIF/DOUBLE')
	if fileTtl > 0:
		for i in range(fileTtl):
			listFilePathName.append("Image/GIF/DOUBLE/Triple_L_Effects_{:02d}.png".format(i))
	return fileTtl

def GetGifFilePathNameList_TRIPLE(listFilePathName):
	if listFilePathName != []:
		listFilePathName.clear()
	fileTtl = GetFilesTtlInDir('Image/GIF/TRIPLE')
	if fileTtl > 0:
		for i in range(fileTtl):
			listFilePathName.append("Image/GIF/TRIPLE/Triple_L_Effects_{:02d}.png".format(i))
	return fileTtl

def GetGifFilePathNameList_BUST(listFilePathName):
	if listFilePathName != []:
		listFilePathName.clear()
	fileTtl = GetFilesTtlInDir('Image/GIF/BUST')
	if fileTtl > 0:
		for i in range(fileTtl):
			listFilePathName.append("Image/GIF/BUST/Broken_A_{:02d}.png".format(i))
	return fileTtl

def GetGifFilePathNameList_Background(listFilePathName, numOfFiles):
	if listFilePathName != []:
		listFilePathName.clear()
	for i in range(numOfFiles):
		listFilePathName.append("Image/GIF/Background/stock-foot-{:02d}.png".format(i))
