#!/usr/bin/env python3
#encoding=utf-8

import string, wcclib

cmds = ['display station all']

def wcc_decode(results):
    "Analyze results and return (MAC, 2.4GHz/5GHz) pair"
    result_lines = results.split(b'\r')
    mac_frequency = {}
    for line in result_lines:
        # Skip lines don't needed
        if (not b'5G' in line and not b'2.4G' in line) or b'Total' in line or b'More' in line:
            continue
        line_split = line.split(None)
	
        mac_origin = line_split[0].decode()
        mac = wcclib.MacFormat(mac_origin)
        frequency_origin = line_split[4].decode()
        if frequency_origin == '5G':
            frequency = '5GHz'
        elif frequency_origin == '2.4G':
            frequency = '2.4GHz'
        else:
            continue
        mac_frequency[mac] = frequency

    return mac_frequency
