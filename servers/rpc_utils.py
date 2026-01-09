import multiprocessing
import os
import requests
import google.generativeai as genai

from dotenv import load_dotenv
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


def solve_math_problem_ai(problem: str) -> str:

    load_dotenv()
    API_KEY = os.getenv("GEMINI_KEY")

    prompt = f"""
    Analise o problema matemático a seguir:
    {problem}

    Determine se o problema é matemático e se pode resultar em um valor numérico único.

    Utilize raciocínio lógico, de cálculo em cálculo, para chegar à resposta.
    Explique os passos da resolução descrevendo o raciocínio no campo "reasoning" da resposta, retorne apenas o resultado final, no formato especificado a seguir. 

    A saída deve ser unicamente no formato JSON:

    Se for um problema matemático:
    {{
        "reasoning": "REASONING...",
        "result": valor,
        "is_math_problem": true
    }}

    Se NÃO for um problema matemático:
    {{
        "reasoning": "",
        "result": null,
        "is_math_problem": false
    }}

    """

    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("models/gemini-3-flash-preview")
        response = model.generate_content(prompt)
        
        return response.text.strip()
    
    except Exception as e:
        print(e)
        return None

#print(solve_math_problem_ai("O céu é azul?"))