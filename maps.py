import urllib.request
import datetime
import os

absPath = f'{os.getcwd()}/img/'
if not os.path.exists(absPath):
    os.mkdir(absPath)

class HourDat():
    def __init__(self, hour, isToday):
        self.hour = hour
        self.isToday = isToday

def isToday(hourNow, hourLimit):
    if hourNow > hourLimit:
        return True
    else:
        return False

def downloadOneStep(arrayHours):
    for hourObj in arrayHours:
        url = f'https://meteoinfo.ru/hmc-input/mapsynop/Analiz{hourObj.hour}h.png'
        # Today or Prevday
        dateForFileName = datetime.date.today() if hourObj.isToday else datetime.date.today() - datetime.timedelta(days=1)
        fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_PR.png'
        urllib.request.urlretrieve(url, fname)

def downloadTwoStep(arrayHours):
    for hourObj in arrayHours:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{hourObj.hour}.png'
        # Today or Prevday
        dateForFileName = datetime.date.today() if hourObj.isToday else datetime.date.today() - datetime.timedelta(days=1)
        fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_K.png'
        urllib.request.urlretrieve(url, fname)

def downloadThreeStep(arrayHours, arrayHeights):
    for hourObj in arrayHours:
        # Today or Prevday
        dateForFileName = datetime.date.today() if hourObj.isToday else datetime.date.today() - datetime.timedelta(days=1)
        for height in arrayHeights:
            url = f'https://meteoinfo.ru/hmc-input/mapsynop/AT-{height}-{hourObj.hour}.png'

            if height % 10 == 0:
                fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_{int(height / 10)}.png'
            else:
                fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_{height}.png'
            urllib.request.urlretrieve(url, fname)                

def oneStep(hourNow):
    arrayHours = [
        HourDat('00',True),
        HourDat('06',isToday(hourNow, 15)),
        HourDat('12',False),
        HourDat('18',False),
        ]
    downloadOneStep(arrayHours)

def twoStep(hourNow):
    arrayHours = [
            HourDat('00',True),
            HourDat('03',isToday(hourNow, 13)),
            HourDat('06',isToday(hourNow, 15)),
            HourDat('09',isToday(hourNow, 17)),
            HourDat('12',False),
            HourDat('15',False),
            HourDat('18',False),
            HourDat('21',False),
        ]
    downloadTwoStep(arrayHours)

def threeStep():
    height = [925, 850, 700, 500, 400, 300, 200, 100]
    arrayHours = [
            HourDat('00',True),
            HourDat('12',False),
        ]
    downloadThreeStep(arrayHours, height)

def main():
    hour_now = datetime.datetime.now().hour
    print(hour_now)

    oneStep(hour_now)
    twoStep(hour_now)
    threeStep(hour_now)


main()