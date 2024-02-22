from phew import logging, server, connect_to_wifi, is_connected_to_wifi, get_ip_address, dns
from phew.template import render_template
import gc

gc.threshold(5000)

domain = "HandyThing"

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
#     return render_template("Auto.html")
    
@server.route("/auto_page",["GET"])
def autohtml(request):
    return render_template("Auto.html")

@server.route("/hotspot_detect", methog["GET"])
def hotspot(request):
    return render_template("loginpico.html")

@server.route("/wrong_host_redirect", method = "GET")
def wrong_host_redirect(request):
    return ("go back to bed")

@server.catchall()
def catch_all(request):
    if request.header.get("host") != domain:
#         return server.redirect("login_page")
        return redircet("https://"+domain+"/wrong_host_redirect")

ap = access_point("Handy Thing v1.1")
ip = ap.ifconfig()[0]
logging.info("DNS started")
dns.run_catchall(ip)
server.run()
logging.info("webserver started")