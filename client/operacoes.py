import ast
import socket
import json
from exceptions import RPCServerNotFound
from datetime import datetime, timedelta

cacheFile = "operations-list.json"

class Operacoes:

    def __init__(self, ns_ip, ns_port, cacheTime: int, usesCache = None):
        self.name_server = (ns_ip, ns_port)
        self.server_address = (None, None)
        self.cache = self.__loadCache()
        self.cacheOperations = usesCache or []
        self.__clearCache(cacheTime)

    def __del__(self):
        with open(cacheFile, 'w') as file:
            json.dump(self.cache, file, indent=4)

    def __loadCache(self):

        try:
            with open(cacheFile, 'r') as file:
                return json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {}

    def __addToCache(self, key, value):
        self.cache[key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }

    def __clearCache(self, cacheTime):

        for key in list(self.cache.keys()):
            time = datetime.fromisoformat(self.cache[key]["timestamp"])
            if datetime.now() - time > timedelta(minutes=cacheTime):
                del self.cache[key]

    def __connect(self):

        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(self.server_address)

            return client
        
        except ConnectionRefusedError as e:
            raise RPCServerNotFound("Erro ao conectar-se ao servidor.", 505)

    def __disconnect(self, client):
        client.close()

    def __getServer(self, name):

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

            s.settimeout(2.0)

            try:

                s.sendto(name.encode(), self.name_server)

                data = s.recv(1024)
                response = data.decode()

                address = ast.literal_eval(response)

                if not isinstance(address, tuple):
                    raise ValueError("Resposta não é uma tupla com o endereço.")

                print("Servidor obtido", address)
                return address
            
            except socket.timeout:
                print("Timeout: o servidor de nome não respondeu")

            except Exception as e:
                print(f"Ocorreu um erro: {e}")
            
            return None


    def __request(self, signature, name, saveInCache = False):

        self.server_address = self.__getServer(name)

        client = self.__connect()
        client.send(signature.encode())

        try:
            res = client.recv(4096).decode()
            self.__disconnect(client)
           
            if name not in ["uolNews", "primes"]:
                value = float(res) if '.' in res else int(res)
            else:
                value = res

            if saveInCache: self.__addToCache(signature, value) 
        
            return value
        
        except Exception as e:
            self.__disconnect(client)
            if saveInCache: self.__addToCache(signature, None)
            return None

    # Decorator
    def useCache(func):
        
        def wrapper(self, *args, **kwargs):
            
            name = func.__name__

            if args:
                signature = f"{name}:{list(args)}"
            else:
                signature = f"{name}"

            if name not in self.cacheOperations:
                return self.__request(signature, name, saveInCache=False)
            
            if signature in self.cache:
                return self.cache[signature]["value"]
            else:
                return self.__request(signature, name, saveInCache=True)

        return wrapper

    @useCache
    def soma(self, *n:int) -> int:
        pass
    
    @useCache
    def fatorial(self, n:int) -> int:
        pass
    
    @useCache
    def subtracao(self, a:int, b:int) -> int:
        pass
    
    @useCache
    def divisao(self, a:float, b:float) -> float:
        pass

    @useCache  
    def multiplicacao(self, a:int, b:int) -> int:
        pass

    @useCache
    def uolNews(self):
        pass

    @useCache
    def primes(self, *n:int):
        pass