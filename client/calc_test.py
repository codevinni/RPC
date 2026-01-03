from operacoes import Operacoes
from exceptions import RPCServerNotFound
import ast
import json

try:

    with open("settings.json") as f:
        settings = json.load(f)
        op = Operacoes(**settings) # Desempacotamento, passa os dados que estão no JSON automaticamente

    print("\n - Soma\n")
    for i in range(0, 5):
        print(f"   {i} + {i*2} + 3 = {op.soma(i, i*2, 3)}")

    print("\n - Subtração\n")
    for i in range(0, 5):
        print(f"   {i*2} - {i} = {op.subtracao(i, i*2)}")
    
    print("\n - Multiplicação\n")
    for i in range(0, 5):
        print(f"   {i+i} x {i} = {op.multiplicacao(i+i, i)}")

    print("\n - Divisão\n")
    for i in range(0, 5):
        print(f"   {i*(2+i)} / {i} = {op.divisao(i*(2+i), i)}")

    print("\n - Fatorial\n")
    for i in range(0, 6):
        print(f"   {i}! = {op.fatorial(i)}")

    print("\n - Ultimas notícias da UOL\n", )
    newsList = ast.literal_eval(op.uolNews())

    for i, n in enumerate(newsList): 
        if len(n): print(f"   {i + 1}. {n}")

    print("\n - Números primos\n")

    prime_matrix = [
        [1, 2, 3],
        [5, 10, 11],
        [7, 9, 6]
    ]

    for l in prime_matrix:
        print(f"   {l}:{op.primes(*l)}")

    print()

except RPCServerNotFound as e:
    print(f"\n{e.msg}\nCódigo de erro: {e.code}\n")
    exit()