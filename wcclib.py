#!/usr/bin/env python
#encoding=utf-8

import paramiko, time, string

def wcc(ip, username, pwd, cmds, brand):
    "Connect to ac and acquire the results of cmds"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, pwd, look_for_keys = False)
        print('Connected. Analyzing......')
        time.sleep(float(1))
        ssh_shell = ssh.invoke_shell()
        results = b'[Begin]'
        for m in cmds:
            res = ssh_shell.sendall(m+'\n')
            time.sleep(float(1))
            result_this = ssh_shell.recv(102400)
            print(result_this)
            results = results + result_this
            while 1:
                if brand == 'cisco':
                    cmd_nextpage = 'y'
                else:
                    cmd_nextpage = ' \n'
                if b'More' in result_this or b'more' in result_this:
                    res = ssh_shell.sendall(cmd_nextpage)
                    time.sleep(float(1))
                    result_this = ssh_shell.recv(102400)
                    print(result_this)
                    results = results + result_this
                else:
                    break
        ssh.close()
        return results
    except:
        return b''

def getDomain(url):
    "Get Domain name from url"
    urlsplit = url.split('/')
    if len(urlsplit) > 2:
        url = urlsplit[2]
    if url.count('@'):
        url = url.split('@')[1]
    if url.count(':'):
        url = url.split(':')[0]
    return url

def getDomains(user):
    "Get domain and topdomain of a user's email address"
    domain = []
    domain.append(user.split('@')[1])
    if '.' in domain[0]:
        if domain[0][len(domain[0]) - 1] != '.':
            domain_tmp = domain[0].split('.')
            domain.append(domain_tmp[len(domain_tmp) - 1].lower())
            return domain
        else:
            return []
    else:
        return []

def getCurTime():
    "Get current time and change it to datatime format"
    t = time.localtime()
    TODAY = "%04d-%02d-%02d"%(t.tm_year, t.tm_mon, t.tm_mday)
    TIME = "%02d:%02d:%02d"%(t.tm_hour, t.tm_min, t.tm_sec)
    return TODAY + ' ' + TIME

def MacFormat(mac, length = 2, separator = ':'):
    "Format any mac address to aa:bb:cc:dd:ee:ff or other lenth and separator"
    new_mac = ''
    j = 0
    if length != 2 and length != 4 and length != 12:
        return 'Length can only be 2, 4 or 12.'
    if separator != ':' and separator != '.' and separator != '-':
        return 'Separator can only be \':\', \'.\' or \'-\'.'

    for i in range(len(mac)):
        if mac[i].isalnum():
            new_mac = new_mac + mac[i]
            j = j + 1
            if not j%length and j != 12:
                new_mac = new_mac + separator
    return new_mac.lower()
