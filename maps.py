import urllib.request
import datetime
import os

# check exist or create folder 'img'
absPath = f'{os.getcwd()}/img/'
if not os.path.exists(absPath):
    os.mkdir(absPath)

class HourDto():
    def __init__(self, hour, isToday):
        self.hour = hour
        self.isToday = isToday

def isToday(hourNow, hourLimit):
    if hourNow > hourLimit:
        return True
    else:
        return False

# download img-Analiz from meteoinfo
# arrayHours - array object HourDto
def downloadOneStep(arrayHours):
    for hourObj in arrayHours:
        url = f'https://meteoinfo.ru/hmc-input/mapsynop/Analiz{hourObj.hour}h.png'
        # Today or Prevday
        dateForFileName = datetime.date.today() if hourObj.isToday else datetime.date.today() - datetime.timedelta(days=1)
        # abs path for save img
        fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_PR.png'
        urllib.request.urlretrieve(url, fname)

# download img-Analiz from meteocenter
# arrayHours - array object HourDto
def downloadTwoStep(arrayHours):
    for hourObj in arrayHours:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{hourObj.hour}.png'
        # Today or Prevday
        dateForFileName = datetime.date.today() if hourObj.isToday else datetime.date.today() - datetime.timedelta(days=1)
        # abs path for save img
        fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_K.png'
        urllib.request.urlretrieve(url, fname)

# download img-AT from meteoinfo
# arrayHours - array object HourDto
# arrayHeights - array heights
def downloadThreeStep(arrayHours, arrayHeights):
    for hourObj in arrayHours:
        # Today or Prevday
        dateForFileName = datetime.date.today() if hourObj.isToday else datetime.date.today() - datetime.timedelta(days=1)
        for height in arrayHeights:
            url = f'https://meteoinfo.ru/hmc-input/mapsynop/AT-{height}-{hourObj.hour}.png'
            if height % 10 == 0:
                # abs path for save img
                fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_{int(height / 10)}.png'
            else:
                # abs path for save img
                fname = f'{absPath}{dateForFileName.strftime("%d%m")}{hourObj.hour}_{height}.png'
            urllib.request.urlretrieve(url, fname)                

# main for download img-Analiz from meteoinfo
def oneStep(hourNow):
    arrayHours = [
        HourDto('00',True),
        HourDto('06',isToday(hourNow, 15)),
        HourDto('12',False),
        HourDto('18',False),
        ]
    downloadOneStep(arrayHours)

# main for download img-Analiz from meteocenter
def twoStep(hourNow):
    arrayHours = [
            HourDto('00',True),
            HourDto('03',isToday(hourNow, 13)),
            HourDto('06',isToday(hourNow, 15)),
            HourDto('09',isToday(hourNow, 17)),
            HourDto('12',False),
            HourDto('15',False),
            HourDto('18',False),
            HourDto('21',False),
        ]
    downloadTwoStep(arrayHours)

# main for download img-AT from meteoinfo
def threeStep():
    height = [925, 850, 700, 500, 400, 300, 200, 100]
    arrayHours = [
            HourDto('00',True),
            HourDto('12',False),
        ]
    downloadThreeStep(arrayHours, height)

def main():
    hour_now = datetime.datetime.now().hour
    print(hour_now)

    oneStep(hour_now)
    twoStep(hour_now)
    threeStep()


main()