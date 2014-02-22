import socks
import socket

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
s = socks.socksocket()
s.connect(('3g2upl4pq6kufc4m.onion', 80))

message = 'GET / HTTP/1.0\r\n\r\n'
s.sendall(message)

reply = s.recv(4069)
print(reply)
