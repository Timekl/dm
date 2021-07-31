import dmPython as dm
import json

dm_conn = dm.connect(user='SYSDBA', password='123456789', server='192.168.43.11', port='5236')
dm_cursor = dm_conn.cursor()

r = '越南进口红心火龙果 2个装 巨无霸大果 单果约600~700g 新鲜水果'
sql_str = "select count(*) from shopping.goods where GOODS_NAME = " + r + ";"
dm_cursor.execute(sql_str)
values = dm_cursor.fetchall()
print(values)
# with open('goods.json', 'w') as f:
#     json.dump(values, f)
dm_cursor.close()
dm_conn.close()
