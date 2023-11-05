__version__ = "0.0.2"

# highly recommended to set a lowish garbage collection threshold
# to minimise memory fragmentation as we sometimes want to
# allocate relatively large blocks of ram.
import gc, os, machine
gc.threshold(50000)

# phew! the Pico (or Python) HTTP Endpoint Wrangler
from . import logging

# determine if remotely mounted or not, changes some behaviours like
# logging truncation
remote_mount = False
try:
  os.statvfs(".") # causes exception if remotely mounted (mpremote/pyboard.py)
except:
  remote_mount = True

def is_connected_to_wifi():
  import network, time
  wlan = network.WLAN(network.STA_IF)
  return wlan.isconnected()

def get_ip_address():
    import network
    try:
        return network.WLAN(network.STA_IF).ifconfig()[0]
    except:
        return None

# helper method to quickly get connected to wifi
def connect_to_wifi(ssid, password, timeout_seconds=30):
  import network, time, machine
  led = machine.Pin('LED', machine.Pin.OUT) #edit for indication

  statuses = {
    network.STAT_IDLE: "idle",
    network.STAT_CONNECTING: "connecting",
    network.STAT_WRONG_PASSWORD: "wrong password",
    network.STAT_NO_AP_FOUND: "access point not found",
    network.STAT_CONNECT_FAIL: "connection failed",
    network.STAT_GOT_IP: "got ip address"
  }

  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)    
  wlan.connect(ssid, password)
  start = time.ticks_ms()
  status = wlan.status()

  logging.debug(f"  - {statuses[status]}")
  while not wlan.isconnected() and (time.ticks_ms() - start) < (timeout_seconds * 1000):
    led.toggle() # builtin led for pico will blink until it is connected to wifi
    new_status = wlan.status()
    if status != new_status:
      logging.debug(f"  - {statuses[status]}")
      status = new_status
    time.sleep(0.25)

  if wlan.status() != 3:
    return None
  else :  #led blink pattern to confirm connection
    led.off()
    time.sleep(0.25)
    for x in range (20):
        led.toggle()
        time.sleep(0.03)
    led.off()
    time.sleep(0.6)
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.6)
    led.on()
    time.sleep(0.05)
    led.off()

  return wlan.ifconfig()[0]

# helper method to put the pico into access point mode
def access_point(ssid, password = None):
  import network

  # start up network in access point mode  
  wlan = network.WLAN(network.AP_IF)
  wlan.config(essid=ssid)
  if password:
    wlan.config(password=password)
  else:    
    wlan.config(security=0) # disable password
  wlan.active(True)

  return wlan
