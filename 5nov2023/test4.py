from phew import logging, server, connect_to_wifi, is_connected_to_wifi
from phew.template import render_template
import network

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
    print(ip)

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
        if username == "Nikhil Motagi" and password == "1234":
            return server.redirect("mode")
            check = 1
        else :
            return "Wrong cridentials", 404
            check = 0

@server.route("/mode",["POST","GET"])
def mode(request):    
    print("Entered mode method")
    print(request)
    if request.method == 'GET':
        print(request.path)
        print("entered get method")
        return render_template("mode.html")
        print("showing request after loading")
        print(request)
    if request.method == 'POST':
        print("Entered post method")
        print(request)

@server.route("/Manual")
def manualmode(request):
    return render_template("manual.html")

@server.route("/automode")
def automode(request):
    return render_template("auto.html")

@server.catchall()
def fault(request):
    return "Page not found", 404

logging.info("Server started")
logging.truncate("log.txt", 500)

server.run()

