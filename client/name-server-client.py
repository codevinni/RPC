import ast
import socket

class NameServerClient():

    def __init__(self):

        self.ip = '127.0.0.1'
        self.port = 9999
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(3.0)

    def askNameServer(self, name) -> tuple:

        try:

            self.sock.sendto(name.encode(), (self.ip, self.port))
            data, addr = self.sock.recvfrom(1024)
            response = data.decode()

            serverAddress = ast.literal_eval(response)
            ip, port = serverAddress[0], serverAddress[1] 

            return ip, port

        except:
            return None