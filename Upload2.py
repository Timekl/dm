import dmPython as dm
from fdfs_client.client import get_tracker_conf, Fdfs_client


def main():
    dm_conn = dm.connect(user='SYSDBA', password='123456789', server='192.168.43.11', port='5236')
    dm_cursor = dm_conn.cursor()
    tracker_conf = get_tracker_conf('fastfdfs_client.conf')
    client = Fdfs_client(tracker_conf)

    for i in range(19):
        for j in range(60):
            k = i * 60 + j + 1
            if k > 1000:
                break
            upload_url = './images2/' + str(i) + '_' + str(j) + '.jpg'
            result = client.upload_by_filename(upload_url)
            url = 'http://xjq.vaiwan.com/' + bytes.decode(result['Remote file_id'])
            sql_str0 = "update shopping.blog set BLOG_IMG_URL = '" + url + "' where BLOG_ID = " + str(k) + ";"
            dm_cursor.execute(sql_str0)
            print(k)

    sql_str1 = 'commit;'
    dm_cursor.execute(sql_str1)
    dm_cursor.close()
    dm_conn.close()


if __name__ == '__main__':
    main()
