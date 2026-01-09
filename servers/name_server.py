from enums import KnownedOperations, Servers
import socket
import random
import threading

class NameServer():

    def __init__(self):

        self.ip = "0.0.0.0"
        self.port = 9999
        self.server = None
        self.names = {
            KnownedOperations.SUM: [Servers.SERVER_1, Servers.SERVER_2],
            KnownedOperations.FATORIAL: [Servers.SERVER_1, Servers.SERVER_2],
            KnownedOperations.SUBTRACTION: [Servers.SERVER_1, Servers.SERVER_2],
            KnownedOperations.DIVISION: [Servers.SERVER_1, Servers.SERVER_2],
            KnownedOperations.MULTIPLY: [Servers.SERVER_1, Servers.SERVER_2],
            KnownedOperations.NEWS: [Servers.SERVER_3],
            KnownedOperations.PRIMES: [Servers.SERVER_3, Servers.SERVER_4],
            KnownedOperations.AI_SOLVER: [Servers.SERVER_4]
        }

    def __pick_random_server(self, operation: KnownedOperations) -> Servers:
        return random.choice(self.names[operation])

    def handle(self, data, clientAddress):

        req = data.decode()
        operation = None

        print(f"\n{clientAddress} asks for {req}")

        for op in KnownedOperations:
            if op.value == req:
                operation = op
                break

        if operation:
            asked_server = self.__pick_random_server(operation)
            response = str(asked_server.value).encode()
        else:
            response = b"Unkown operation"
        
        print(f"   > Response: {response.decode()}\n")
        self.server.sendto(response, clientAddress)


    def run(self):
    
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as self.server:
            
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind((self.ip, self.port))
            print(f"\nName server iniciado em {self.ip}:{self.port}")

            while True:
                
                data, clientAddress = self.server.recvfrom(1024)
                
                t = threading.Thread(target=self.handle, args=(data, clientAddress))
                t.start()

NameServer().run()