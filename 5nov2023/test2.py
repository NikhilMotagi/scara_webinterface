from phew import logging, server, connect_to_wifi, is_connected_to_wifi
from phew.template import render_template
import network

wlan = network.WLAN(network.STA_IF)
ssid = "Redmi Note 11"
password = "12345678"
ip = ""
# connect_to_wifi(ssid,password)
if (is_connected_to_wifi() == False):
    ip = connect_to_wifi(ssid,password)
    logging.info(ip)
    logging.info("Pico connected")
#   print(wlan.ifconfig()[0])
else :
    logging.info("Pico has already been connected")
    print(ip)

@server.route("/")
def index(request):
    return render_template("loginpico.html")

@server.route("/manualmode")
def index(request):
    return render_template("manual.html")

@server.catchall()
def fault(request):
    return "Page not found", 404

logging.info("Server started")
logging.truncate("log.txt", 500)

server.run()

