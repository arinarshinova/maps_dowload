import urllib.request
import datetime
import ssl


now = datetime.datetime.now()
hour_now = now.hour
print(hour_now)

if hour_now > 15:
    prizem_t = ['00', '06']
    prizem_y = ['12', '18']

    for i in prizem_t:
        url = f'https://meteoinfo.ru/hmc-input/mapsynop/Analiz{i}h.png'
        fname = f'{datetime.date.today().strftime("%d%m")}{i}_PR.png'
        urllib.request.urlretrieve(url,fname)

    for i in prizem_y:
        url = f'https://meteoinfo.ru/hmc-input/mapsynop/Analiz{i}h.png'
        fname = f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_PR.png'
        urllib.request.urlretrieve(url,fname)
else:
    prizem_t = ['00']
    prizem_y = ['06', '12', '18']

    for i in prizem_t:
        url = f'https://meteoinfo.ru/hmc-input/mapsynop/Analiz{i}h.png'
        fname = f'{datetime.date.today().strftime("%d%m")}{i}_PR.png'
        urllib.request.urlretrieve(url,fname)

    for i in prizem_y:
        url = f'https://meteoinfo.ru/hmc-input/mapsynop/Analiz{i}h.png'
        fname = f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_PR.png'
        urllib.request.urlretrieve(url,fname)


if hour_now > 17:
    rotate_t = ['00', '03', '06', '09']
    rotate_y = ['12', '15', '18', '21']
    for i in rotate_t:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url, f'{datetime.date.today().strftime("%d%m")}{i}_K.png')

    for i in rotate_y:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url,f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_K.png')
elif hour_now > 15:
    rotate_t = ['00', '03', '06']
    rotate_y = ['09', '12', '15', '18', '21']
    for i in rotate_t:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url, f'{datetime.date.today().strftime("%d%m")}{i}_K.png')

    for i in rotate_y:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url,f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_K.png')
elif hour_now > 13:
    rotate_t = ['00', '03']
    rotate_y = ['06', '09', '12', '15', '18', '21']
    for i in rotate_t:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url, f'{datetime.date.today().strftime("%d%m")}{i}_K.png')

    for i in rotate_y:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url,
                                   f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_K.png')
else:
    rotate_t = ['00']
    rotate_y = ['03', '06', '09', '12', '15', '18', '21']
    for i in rotate_t:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url, f'{datetime.date.today().strftime("%d%m")}{i}_K.png')

    for i in rotate_y:
        url = f'http://www.meteocenter.net/circ/rotate/UNTT{i}.png'
        urllib.request.urlretrieve(url,
                                   f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_K.png')

hours = ['00', '12']
height = [925, 850, 700, 500, 400, 300, 200, 100]

for i in hours:
    if i == '00':
        for k in height:
            url = f'https://meteoinfo.ru/hmc-input/mapsynop/AT-{k}-{i}.png'
            if k % 10 == 0:
                fname = f'{datetime.date.today().strftime("%d%m")}{i}_{int(k / 10)}.png'
            else:
                fname = f'{datetime.date.today().strftime("%d%m")}{i}_{k}.png'
            urllib.request.urlretrieve(url,fname)
    else:
        for k in height:
            url = f'https://meteoinfo.ru/hmc-input/mapsynop/AT-{k}-{i}.png'
            if k % 10 == 0:
                fname = f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_{int(k / 10)}.png'
            else:
                fname = f'{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%d%m")}{i}_{k}.png'
            urllib.request.urlretrieve(url,fname)