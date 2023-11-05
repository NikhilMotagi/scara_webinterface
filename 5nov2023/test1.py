from phew import connect_to_wifi,is_connected_to_wifi
import network

wlan = network.WLAN(network.STA_IF)

connect_to_wifi("Redmi Note 11","12345678")

if(is_connected_to_wifi()):
    print("conneted")
    print(wlan.ifconfig()[0])
else:
    print("doomed")