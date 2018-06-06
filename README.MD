## WCC - WLAN Client Collection

The program is to collect the information of WLAN client's capable of 2.4GHz / 5GHz connection. The method is easy: Connect to WLAN Access Controller (AC) by SSH, use CMDs to show information and collect the client's Band/Channel/Wireless mode. If a client always assciates AP with 2.4GHz channel or 802.11bg/802.11gn mode and never show up in 5GHz, it is obviously the client only supports 2.4GHz. Once a client connects AP with 5GHz channel, we know the client supports 5GHz.

The program supports Aruba, Cisco, Huawei, H3C and Ruijie AC. All (MAC, Frequency) pairs are stored in JSON file.

### How to play.
Note: python-paramiko is needed.
1. Edit ac.py to add your ACs.
2. Run wcc.py to collect client information from ACs in ac.py and the results are stored in wcc_result.json.
   Next time you run wcc.py, it will load wcc_result.json and update 2.4GHz/5GHz capable of clients.
   So better to add the program to crontab to run periodically.
3. You can also run csv_dump.py to dump wcc_result.json to csv format for easy use.

### Known issues.
1. Cisco WLC sometimes raises error "Raw mode will not be supported, Closing connection" . There is no solution atm, just skip the error by return empty to results.
