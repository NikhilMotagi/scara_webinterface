from phew import logging, server, is_connected_to_wifi, connect_to_wifi, get_ip_address
from phew.template import render_template
import network
import socket

# setting up wifi configuration
wlan = network.WLAN(network.STA_IF)

#list of networks it can connect to, you can add yours
ssid = "Redmi Note 11"
ssid1 = "Airtel-E5573-DD7F"
password = "12345678"
password1 = "fq5d7qhf"

# connect_to_wifi(ssid,password)
if (is_connected_to_wifi() == False):
    # keep in mind to change ssid and password variables according to current requirement
    logging.info(connect_to_wifi(ssid1,password1))
    logging.info("Pico connected")
else :
    logging.info("Pico has already been connected")
    logging.info(get_ip_address())


#--------------------------------------------------------------------#
#these are the routes that our project wbepage will follow
# "/" is our login and the first page to render bydefault
# "/mode" is our mode selection page. This is the most troublesum page so
# please do no tinker with it :`(
# "/Manual" is the manual page, it wil render manual.html. Idea with this page is that
# each button gets it own xml request, parsing that request we can use route funcitons
# to perform desired axis motion.
# "/Auto" is our autopage. I had to do a workaorund by redirecting it no another route
# because for some reason it could not forget my last code which was pthetic :(

@server.route("/",["POST","GET"])
def login(request):
    print(request)
    global username
    if request.method == 'GET':
        return render_template("login.html")
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
def mode(request):
    print(f"Request path :"+request.uri)
#     print(response)
    return render_template("mode.html", platform_username = username)
    
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
    return render_template("Auto.html")
#     return server.redirect("auto_page")
#     return "hello"
    
@server.route("/auto_page",["GET"])
def autohtml(request):
    return render_template("Auto.html")


# catchall route is used to handle any failed request
@server.catchall()
def fault(request):
    return "Page not found", 404

logging.info("Server started")

# truncate functino helps to keep log file small
logging.truncate("log.txt", 500)

server.run()
