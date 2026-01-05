import multiprocessing
import requests
from lxml import etree

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