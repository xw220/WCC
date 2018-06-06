#!/usr/bin/python3
#encoding=utf-8

import os, json

cur_path = os.path.dirname(__file__)
with open(cur_path + '/wcc_result.json','r') as f:
    wcc_result = json.load(f)

with open(cur_path + '/mac_frequency.csv', 'w') as f:
    mac_low_count = 0
    mac_high_count = 0
    for mac in wcc_result:
        if wcc_result[mac] == '5GHz':
            mac_high_count += 1
        elif wcc_result[mac] == '2.4GHz':
            mac_low_count += 1
        f.write(mac+','+wcc_result[mac]+'\n')
print('MACs total:\t', len(wcc_result))
print('2.4GHz:\t\t', mac_low_count)
print('5GHz:\t\t',mac_high_count)
ratio = mac_low_count / len(wcc_result)
print('2.4GHz Ratio:\t',"%.2f%%"%(ratio*100))
