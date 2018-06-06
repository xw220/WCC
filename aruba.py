#!/usr/bin/env python3
#encoding=utf-8

import string

def gen_cmds(enable_pwd):
    cmds = ['enable',enable_pwd,'show station-table']
    return cmds

def wcc_decode(results):
    "Analyze results and return (MAC, 2.4GHz/5GHz) pair"
    result_lines = results.split(b'\r')
    mac_frequency = {}
    for line in result_lines:
        # Skip lines don't needed
        if not b':' in line or b'MAC' in line or b'Password' in line or b'Station' in line or b'login' in line:
            continue
        line_split = line.split(None)

        mac = line_split[0].decode()
        if ':' in mac:
            if line_split[7] == b'No' or line_split[7] == b'Yes':
                wireless_mode = line_split[6].decode()
            elif line_split[8] == b'No' or line_split[8] == b'Yes':
                wireless_mode = line_split[7].decode()
            else:
                continue
        else:
            continue
		
        if 'a' in wireless_mode:
            mac_frequency[mac] = '5GHz'
        else:
            mac_frequency[mac] = '2.4GHz'

    return mac_frequency
