import os
import time
import requests
import re
import json
import math
import _thread
from pathlib import Path


def goods_open():
    with open('goods.json') as f:
        values = json.load(f)
    return values


def pc(values):
    for name in values:
        name_1 = './images/'
        name = name[0]

        if '/' in name:
            name = name.replace('/', '')
        if '\\' in name:
            name = name.replace('\\', '')
        if ':' in name:
            name = name.replace(':', '')
        if '*' in name:
            name = name.replace('*', '')
        if '?' in name:
            name = name.replace('?', '')
        if '"' in name:
            name = name.replace('"', '')
        if '<' in name:
            name = name.replace('<', '')
        if '>' in name:
            name = name.replace('>', '')
        if '|' in name:
            name = name.replace('|', '')

        dd = Path(name_1+name+'.jpg')
        if dd.exists():
            continue

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + name + '&pn=0'
        res = requests.get(url, headers=headers)
        htlm_1 = res.content.decode()
        a = re.findall('"objURL":"(.*?)",', htlm_1)
        if a == []:
            for i in range(len(name)):
                names = name[:-(i + 1)]
                url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + names + '&pn=0'
                res = requests.get(url, headers=headers)
                htlm_1 = res.content.decode()
                a = re.findall('"objURL":"(.*?)",', htlm_1)
                if a != []:
                    break
            if a == []:
                continue

        img = requests.get(a[0])
        f = open(name_1 + name + '.jpg', 'ab')
        f.write(img.content)
        f.close()


if __name__ == '__main__':
    values = goods_open()
    values = values
    length = len(values)
    n = 1
    for i in range(n):
        value = values[math.floor(i / n * length):math.floor((i + 1) / n * length)]
        _thread.start_new_thread(pc, (value,))

    path = './images'
    _a = -1
    while (1):
        a = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
        if (a == _a and a == 51075):
            break
        _a = a
        print(a)
        time.sleep(20)
    print(a)
