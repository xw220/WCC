#!/usr/bin/env python3
#encoding=utf-8

import string, wcclib

def gen_cmds_2dot4g(enable_pwd):
    cmds = ['super',enable_pwd,'display wlan client frequency-band 2.4']
    return cmds

def gen_cmds_5g(enable_pwd):
    cmds = ['super',enable_pwd,'display wlan client frequency-band 5']
    return cmds

def wcc_decode(results,frequency):
    "Analyze results and return (MAC, 2.4GHz/5GHz) pair"
    result_lines = results.split(b'\r')
    mac_frequency = {}
    for line in result_lines:
        # Skip lines don't needed
        if not b'-' in line or b'More' in line or b'User' in line or b'display' in line or b'*' in line:
            continue
        line_split = line.split(None)
	
        mac_origin = line_split[0].decode()
        if mac_origin:
            mac = wcclib.MacFormat(mac_origin)
            mac_frequency[mac] = frequency

    return mac_frequency
