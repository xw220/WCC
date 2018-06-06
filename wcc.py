#!/usr/bin/env python3
#encoding=utf-8

import os, time, json, string
import ac, wcclib
import aruba, h3c, huawei, cisco, ruijie

if __name__ == '__main__':
    mac_frequency = {}
    for nas in ac.aclist:
        ip = nas
        username = ac.aclist[ip]['username']
        pwd = ac.aclist[ip]['pwd']
        enable_pwd = ac.aclist[ip]['enable_pwd']
        brand = ac.aclist[ip]['brand']
	
        print('Connecting to ' + brand + ' ac ' + ip + '......')
        if brand == 'aruba':
            cmds = aruba.gen_cmds(enable_pwd)
            results = wcclib.wcc(ip, username, pwd, cmds, brand)
            mac_frequency.update(aruba.wcc_decode(results))
        elif brand == 'h3c':
            cmds = h3c.gen_cmds_2dot4g(enable_pwd)
            results = wcclib.wcc(ip, username, pwd, cmds, brand)
            mac_frequency.update(h3c.wcc_decode(results, '2.4GHz'))
            cmds = h3c.gen_cmds_5g(enable_pwd)
            results = wcclib.wcc(ip, username, pwd, cmds, brand)
            mac_frequency.update(h3c.wcc_decode(results, '5GHz'))
        elif brand == 'huawei':
            cmds = huawei.cmds
            results = wcclib.wcc(ip, username, pwd, cmds, brand)
            mac_frequency.update(huawei.wcc_decode(results))
        elif brand == 'cisco':
            cmds = cisco.gen_cmds(username, pwd)
            results = wcclib.wcc(ip, username, pwd, cmds, brand)
            mac_frequency.update(cisco.wcc_decode(results))
        elif brand == 'ruijie':
            cmds = ruijie.cmds
            results = wcclib.wcc(ip, username, pwd, cmds, brand)
            mac_frequency.update(ruijie.wcc_decode(results))

    cur_path = os.path.dirname(__file__) 
    with open(cur_path+'/wcc_result.json','r') as f:
        wcc_result = json.load(f)
    if wcc_result:
        for mac in mac_frequency:
            if mac in wcc_result:
                if wcc_result[mac] == '5GHz':
                    continue
                elif mac_frequency[mac] == '5GHz':
                    wcc_result[mac] = '5GHz'
                else:
                    continue
            else:
                wcc_result[mac] = mac_frequency[mac]
    else:
        wcc_result = mac_frequency

    with open(cur_path+'/wcc_result.json','w') as f:
        json.dump(wcc_result, f)

