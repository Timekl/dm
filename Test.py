import json
import os
from pathlib import Path

with open('goods.json') as f:
    k = json.load(f)

r = list()
for ii in k:
    i = ii[0]
    if "'" in ii[0]:
        print('1:' + ii[0])
        ii0 = ii[0].replace("'", "''")
        print('4:' + ii0)
        break

    # if '/' in i:
    #     i = i.replace('/', '')
    # if '\\' in i:
    #     i = i.replace('\\', '')
    # if ':' in i:
    #     i = i.replace(':', '')
    # if '*' in i:
    #     i = i.replace('*', '')
    # if '?' in i:
    #     i = i.replace('?', '')
    # if '"' in i:
    #     i = i.replace('"', '')
    # if '<' in i:
    #     i = i.replace('<', '')
    # if '>' in i:
    #     i = i.replace('>', '')
    # if '|' in i:
    #     i = i.replace('|', '')
    # dd = Path('./images/' + i + '.jpg')
    # if not dd.exists():
    #     print(i)

# for i in range(len(k)):
#     r = k[i][0]
#     if '/' in r:
#         r = r.replace('/', '')
#     if '\\' in r:
#         r = r.replace('\\', '')
#     if ':' in r:
#         r = r.replace(':', '')
#     if '*' in r:
#         r = r.replace('*', '')
#     if '?' in r:
#         r = r.replace('?', '')
#     if '"' in r:
#         r = r.replace('"', '')
#     if '<' in r:
#         r = r.replace('<', '')
#     if '>' in r:
#         r = r.replace('>', '')
#     if '|' in r:
#         r = r.replace('|', '')
#     if r == '#NAME':
#         print(i)
#         print(k[i])

# path = './images/'
# a = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
# print(a)
