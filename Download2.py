import re

import requests


def dl():
    name_1 = './images2/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    k = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    for i in k:
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + '美图' + '&pn=' + str(i)
        res = requests.get(url, headers=headers)
        htlm_1 = res.content.decode()
        a = re.findall('"objURL":"(.*?)",', htlm_1)
        k = 0
        for j in a:
            img = requests.get(j)
            f = open(name_1 + str(i) + '_' + str(k) + '.jpg', 'ab')
            print(str(i) + '_' + str(k))
            f.write(img.content)
            f.close()
            k = k + 1


if __name__ == '__main__':
    dl()
