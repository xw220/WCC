#!/usr/bin/env python3
#encoding=utf-8

import string, wcclib

cmds = ['show ac-config client']

def wcc_decode(results):
    "Analyze results and return (MAC, 2.4GHz/5GHz) pair"
    result_lines = results.split(b'\n')
    mac_frequency = {}
    for line in result_lines:
        # Skip lines don't needed
        if not b'/' in line or b'More' in line or b'ap name' in line or b'Status' in line:
            continue
        mac_origin = line[0:14].decode()
        line_split = line[31:len(line)].split(None)
        status = line_split[3].decode().split('/')[2]
        if status == 'ac' or status == 'an':
            frequency = '5GHz'
        else:
            frequency = '2.4GHz'
        if mac_origin:
            mac = wcclib.MacFormat(mac_origin)
            mac_frequency[mac] = frequency

    return mac_frequency
