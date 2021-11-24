"""
Ngrok Web Manager
Github: @thisiskeanyvy
Instgram: @thisiskeanyvy
Twitter: @thisiskeanyvy
"""

import os, socket, threading
from time import *
from set import *
from webserver import *
from pyngrok import ngrok, conf

#background jobs
webserver_start = threading.Thread(target=webserver_start, name="Ngrok Web Manager")

def main():
    set_clear()
    webserver_start.start()
    public_admin()
    tunnel_status()

def public_admin():
    public_tunnel_url = ngrok.connect(5000, "http").public_url
    print(f"Admin interface : {public_tunnel_url.replace('http','https')}")

def conf():
    ngrok.set_auth_token("yourtoken")
    conf.get_default().region = "fr"

def type():
    if type == "ssh":
        port = 22
        protocol = "tcp"
    elif type == "http":
        port = 80
        protocol = "http"
    else:
        port = "customport"
        protocol = "customport"

def tunnel_status():
    ngrok.get_tunnels()

def authtoken():
    ngrok.set_auth_token("")

def tunnel_start():
    global tunnel_url
    try:
        tunnel_url = ngrok.connect(80, "http").public_url
        print(tunnel_url)
    except KeyboardInterrupt:
        print("Stopping ngrok service...")
        ngrok.kill()

def tunnel_stop():
    ngrok.disconnect(tunnel_url)

if __name__ == "__main__":
    main()
