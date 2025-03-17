# pylint: skip-file

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import network
import webrepl
import gc
import esp
import time

esp.osdebug(0)

gc.enable()

webrepl.start()

try:
    with open("wifisecret.txt") as fi:
        data = fi.read().split(",")
        mode, wifissid, wifipass = data[0], data[1], data[2]
except:
    mode = 'AP'

try:
    if mode == 'AP':
        ap = network.WLAN(network.AP_IF)
        ap.config(essid='ESPemma')
        ap.active(True)
    else:
        lan = network.WLAN(network.STA_IF)
        lan.active(True)
        lan.connect(wifissid, wifipass)
        start = time.time()
        while not lan.isconnected():
            time.sleep(0.1)
            if (time.time() - start) > 10:
                raise TimeoutError
except:
    ap = network.WLAN(network.AP_IF)
    ap.config(essid='ESPemma.err')
    ap.active(True)

gc.collect()