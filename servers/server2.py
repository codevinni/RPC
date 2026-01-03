import ast
import json
import math
import multiprocessing
import socket
import sys
import requests
from lxml import etree

cacheFile = "server2Op-list.json"
MAX_CACHE_SIZE = 1000

def cacheSize(cache):
    return len(json.dumps(cache))

def loadCache():

        try:
            with open(cacheFile, 'r') as file:
                return json.load(file)

        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return {}

def __addToCache(cache, key, value):
    cache[key] = value

def sub(a, b):
    return a - b if a > b else b - a # Equivalente ao ternário em c

def getNews():

    URL = "https://www.uol.com.br/vueland/api/?loadComponent=XmlFeedRss"
    req = requests.get(URL)
    news = []

    if req:
        
        xml = etree.fromstring(req.content)
        
        for e in xml.iter():
            if e.tag == "item":

                title = e.find("description")

                if title is not None and title.text:
                    news.append(title.text)

    return news

def is_prime(n):

    is_prime = True

    for i in range(1, n + 1):
        if (i != 1 and i != n) and n % i == 0:
            is_prime = False
            break

    return is_prime

def check_primes(numbers: list):

    with multiprocessing.Pool(processes=4) as pool:
        result = pool.map(is_prime, numbers)

    return result

def run():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        cache = loadCache()
        ip = "127.0.0.1"
        port = 8502

        server.bind((ip, port))
        server.listen(0)

        while True:

            clientSocket, clientAddress = server.accept()
            req = clientSocket.recv(1024)

            try:
                
                sys.set_int_max_str_digits(1000000)
                func = req.decode().split(':')

                op = func[0]
                args = ast.literal_eval(func[1]) if op != "uolNews" else None # Converte uma string que é uma lista literal em uma lista msm
                signature = f'{op}{args if args else ""}'
                
                print(f"{clientAddress[0]} -> {signature}")

                if signature not in cache:
                
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
                    if op != "uolNews": __addToCache(cache, signature, result)
                   
                    # Inválidar cache
                    while cacheSize(cache) > MAX_CACHE_SIZE:
                        if cache:
                            del cache[next(iter(cache))]
                            '''
                                del: apaga chaves ou items
                                next: obtem o próximo item de um iterador (nesse caso, o primeiro)
                                iter: converte um objeto iterável em iterador
                            '''
    
                    clientSocket.send(response.encode())
                else:
                    print(" > from cache")
                    clientSocket.send(str(cache[signature]).encode())

                print(f"Success\n")

            except Exception as e:
                print(e)
                print(f"Failed\n")
                pass

            with open(cacheFile, 'w') as file:
                json.dump(cache, file, indent=4)

            clientSocket.close()

run()