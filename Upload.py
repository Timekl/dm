import _thread
import math
import time
from pathlib import Path
from fdfs_client.client import get_tracker_conf, Fdfs_client
import dmPython as dm
import json


def goods_open():
    with open('goods.json') as f:
        values = json.load(f)
    return values


def upload(values):
    dm_conn = dm.connect(user='SYSDBA', password='123456789', server='192.168.43.11', port='5236')
    dm_cursor = dm_conn.cursor()
    tracker_conf = get_tracker_conf('fastfdfs_client.conf')
    client = Fdfs_client(tracker_conf)

    for value in values:
        name = value[0]
        if "'" in value[0]:
            value0 = value[0].replace("'", "''")
        else:
            value0 = value[0]
        sql_str0 = "select GOODS_IMG_URL from shopping.goods where GOODS_NAME = '" + value0 + "';"
        dm_cursor.execute(sql_str0)
        kk = dm_cursor.fetchall()
        if kk[0][0] != 'http://xjq.vaiwan.com/group1/M00/00/00/wKgrZWDnxnCAFigkAASZZuAdJtY782.jpg':
            continue

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
        if '.' in name:
            name = name.replace('.', '_')

        # dd = Path('./images/' + name + '.jpg')
        # if dd.exists():
        result = client.upload_by_filename('./images/' + name + '.jpg')
        url = 'http://xjq.vaiwan.com/' + bytes.decode(result['Remote file_id'])
        sql_str = "update shopping.goods set GOODS_IMG_URL = '" + url + "' where GOODS_NAME = '" + value0 + "';"
        dm_cursor.execute(sql_str)

    sql_str2 = 'commit;'
    dm_cursor.execute(sql_str2)
    dm_cursor.close()
    dm_conn.close()


if __name__ == '__main__':
    values = goods_open()
    values = values
    length = len(values)
    n = 10
    for i in range(n):
        value = values[math.floor(i / n * length):math.floor((i + 1) / n * length)]
        _thread.start_new_thread(upload, (value,))

    dm_conn2 = dm.connect(user='SYSDBA', password='123456789', server='192.168.43.11', port='5236')
    dm_cursor2 = dm_conn2.cursor()
    while 1:
        sql_str_ = "select count(*) from shopping.goods where GOODS_IMG_URL = 'http://xjq.vaiwan.com/group1/M00/00/00/wKgrZWDnxnCAFigkAASZZuAdJtY782.jpg';commit;"
        dm_cursor2.execute(sql_str_)
        num = dm_cursor2.fetchall()[0][0]
        if num == 0:
            break
        print(num)
        time.sleep(20)
