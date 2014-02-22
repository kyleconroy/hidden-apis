# Python 

Make sure that you have an active connection to the TOR network.
Follow these guides:

- Setting up TOR on your desktop
- Setting up TOR on your server

We'll be connecting to the DuckDuckGo Instant Answer API

    http://3g2upl4pq6kufc4m.onion/?q=define+ostensibly&format=json

## Prerequisites

    pip install PySocks

### Connect using `socket`

```python
import socks
import socket

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
s = socks.socksocket()
s.connect(('3g2upl4pq6kufc4m.onion', 80))

message = 'GET / HTTP/1.0\r\n\r\n'
s.sendall(message)

reply = s.recv(4069)
print(reply)
```

### Connect using `urllib2`

We have to monkey patch here because urllib uses a different module or
something for DNS resolution, even though we set `rdns` lookup to `True`.

```python
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
```

### Connect using `requests`

Requests does not support SOCKS proxies. Track progress by following these
issues

- https://github.com/shazow/urllib3/pull/284
