from phew import logging, server, is_connected_to_wifi, connect_to_wifi, get_ip_address
from phew.template import render_template
import network
import socket


wlan = network.WLAN(network.STA_IF)
ssid = "Redmi Note 11"
ssid1 = "Airtel-E5573-DD7F"
password = "12345678"
password1 = "fq5d7qhf"
# ip = ""
global check
# connect_to_wifi(ssid,password)
if (is_connected_to_wifi() == False):
    logging.info(connect_to_wifi(ssid1,password1))
    logging.info("Pico connected")
#   print(wlan.ifconfig()[0])
else :
    logging.info("Pico has already been connected")
    logging.info(get_ip_address())

@server.route("/",["POST","GET"])
def login(request):
    print(request)
    if request.method == 'GET':
        return render_template("loginpico.html")
    if request.method == 'POST':
        username = request.form.get("text",None)
        password = request.form.get("pswd",None)
#         print(username)
#         print(password)
        if username == "user1" and password == "1234":
            return server.redirect("mode")
        else :
            return "Wrong cridentials", 404

@server.route("/mode",["POST","GET"])
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
    return server.redirect("auto_page")
#     return "hello"
    
@server.route("/auto_page",["GET"])
def autohtml(request):
    return render_template("Auto.html")

@server.catchall()
def fault(request):
    return "Page not found", 404

logging.info("Server started")
logging.truncate("log.txt", 500)

server.run()


