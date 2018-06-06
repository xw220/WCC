#!/usr/bin/env python3
#encoding=utf-8

import string

def gen_cmds(username, pwd):
    cmds = [username,pwd,'show client summary']
    return cmds

def wcc_decode(results):
    "Analyze results and return (MAC, 2.4GHz/5GHz) pair"
    result_lines = results.split(b'\r')
    mac_frequency = {}
    for line in result_lines:
        # Skip lines don't needed
        if not b'802.11' in line:
            continue
        line_split = line.split(None)
        mac = line_split[0].decode()
        frequency_origin = line_split[6]
        if b'5' in frequency_origin:
            frequency = '5GHz'
        elif b'2.4' in frequency_origin or b'802.11g' in frequency_origin or b'802.11b' in frequency_origin:
            frequency = '2.4GHz'
        else:
            continue
        mac_frequency[mac] = frequency

    return mac_frequency
