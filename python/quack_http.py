import socket
import pprint
import json
import socks
import urllib2

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

# Gotta' Monkey Patch 'Em Al
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150, True)
socket.socket = socks.socksocket
socket.create_connection = create_connection

resp = urllib2.urlopen("http://3g2upl4pq6kufc4m.onion/?q=define+ostensibly&format=json")

pprint.pprint(json.load(resp))
