import socket
import threading
from GETPARAMS import _ai_org_data
from GETPARAMS import _tcpport
from GETPARAMS import _tcphost

class ThreadedServer(object):
    def __init__(self):
        self.host = _tcphost
        self.port = _tcpport
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient, args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    #protocol command
                    if response.decode("utf-8") =="++GAI":
                        client.send(str(_ai_org_data[0][0]).encode())
                else:
                    raise socket.error('Client disconnected')

            except Exception as e:
                print(str(e))
                client.close()
                return False