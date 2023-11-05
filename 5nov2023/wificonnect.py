import machine
import socket
import math
import utime
import network
import time
wlan = network.WLAN(network.STA_IF)
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("Redmi Note 11","12345678")

def wifi_status():
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        print('waiting for connection...')
        time.sleep(1)
    
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
    else:
        print('connected')
        ip=wlan.ifconfig()[0]
        print('IP: ', ip)
    return(ip)
