import ast
import json
import math
import socket
import sys

from rpc_utils import *

class RPCServer():

    def __init__(self, ip:str, port:int, cacheFilename:str, maxCacheSize:int, allowedOps:list = None):
        self.ip = ip
        self.port = port
        self.cacheFilename = cacheFilename
        self.maxCacheSize = maxCacheSize
        self.allowedOps = allowedOps
        self.cache = {}

    def __getCacheSize(self):
        return len(json.dumps(self.cache))

    def __loadCache(self):

        try:
            with open(self.cacheFilename, 'r') as file:
                self.cache = json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return

    def __addToCache(self, key, value):
        self.cache[key] = value

    def run(self):

        sys.set_int_max_str_digits(1000000)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.__loadCache()
            server.bind((self.ip, self.port))
            server.listen(0)

            while True:

                clientSocket, clientAddress = server.accept()
                req = clientSocket.recv(1024)

                try:
                    
                    func = req.decode().split(':')
                    op = func[0]

                    if self.allowedOps is not None and op not in self.allowedOps:
                        clientSocket.send(b"Operacao nao permitida")
                        clientSocket.close()
                        continue

                    args = ast.literal_eval(func[1]) if op != "uolNews" else None # Converte uma string que é uma lista literal em uma lista msm
                    signature = f'{op}{args if args else ""}'
                    
                    print(f"{clientAddress[0]} -> {signature}")

                    if signature not in self.cache:
                    
                        print(' > calculated')
                        result = None

                        if op == "soma":
                            result = sum(args)

                        elif op == "fatorial":
                            if len(args) == 1:
                                result = math.factorial(args[0])

                        elif op == "subtracao":
                            if len(args) == 2:
                                result = sub(args[0], args[1])

                        elif op == "divisao":
                            if len(args) == 2:
                                result = args[0] / args[1]

                        elif op == "multiplicacao":
                            if len(args) == 2:
                                result = args[0] * args[1]
                        
                        elif op == "uolNews":
                            result = getNews()[:10]

                        elif op == "primes":
                            result = check_primes(args)
                            print(f"PRIMES: {result}")

                        response = str(result)
                        if op != "uolNews": self.__addToCache(signature, result)
                    
                        # Inválidar cache
                        while self.__getCacheSize() > self.maxCacheSize:
                            if self.cache:
                                del self.cache[next(iter(self.cache))]
                                '''
                                    del: apaga chaves ou items
                                    next: obtem o próximo item de um iterador (nesse caso, o primeiro)
                                    iter: converte um objeto iterável em iterador
                                '''
        
                        clientSocket.send(response.encode())
                    else:
                        print(" > from cache")
                        clientSocket.send(str(self.cache[signature]).encode())

                    print(f"Success\n")

                except Exception as e:
                    print(e)
                    print(f"Failed\n")
                    pass

                with open(self.cacheFilename, 'w') as file:
                    json.dump(self.cache, file, indent=4)

                clientSocket.close()