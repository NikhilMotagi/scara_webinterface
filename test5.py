from phew import logging, server, connect_to_wifi, is_connected_to_wifi, get_ip_address
from phew.template import render_template
import network
import socket


wlan = network.WLAN(network.STA_IF)
ssid = "Redmi Note 11"
password = "12345678"
ip = ""
global check
# connect_to_wifi(ssid,password)
if (is_connected_to_wifi() == False):
    ip = connect_to_wifi(ssid,password)
    logging.info(ip)
    logging.info("Pico connected")
#   print(wlan.ifconfig()[0])
else :
    logging.info("Pico has already been connected")
    logging.info(get_ip_address())

@server.route("/",["POST","GET"])
def login(request):
    print(f"Request path :"+request.uri)
#     print(response)
    return render_template("mode.html")
    
@server.route("/Manual",["POST","GET"])
def manual(request):
    print(request)
    print(f"Request method: "+ request.uri)
    print("finally here")
    return render_template("manual.html")

@server.route("/Auto",["POST","GET"])
def auto(request):
    print(request)
    print(f"Request method: "+ request.uri)
    print("in auto mode")
    if (request.method == "GET"):
        print("about to render auto page")
        return render_template("auto.html")
    else:
        print("maybe method is POST")
        return "get a auto page "

@server.catchall()
def fault(request):
    return "Page not found", 404

logging.info("Server started")
logging.truncate("log.txt", 500)

server.run()


