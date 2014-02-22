import socket
import pprint
import json
import socks
import urllib2

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket

resp = urllib2.urlopen("http://3g2upl4pq6kufc4m.onion/?q=define+ostensibly&format=json")

pprint.pprint(json.load(resp))
