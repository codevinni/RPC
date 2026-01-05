from enum import Enum

class KnownedOperations(Enum):
    SUM = "soma"
    FATORIAL = "fatorial"
    SUBTRACTION = "subtracao"
    DIVISION = "divisao"
    MULTIPLY = "multiplicacao"
    NEWS = "uolNews"
    PRIMES = "primes"
    AI_SOLVER = "mathSolverAi"

class Servers(Enum):

    SERVER_1 = ("127.0.0.1", 8501)
    SERVER_2 = ("127.0.0.1", 8502)
    SERVER_3 = ("127.0.0.1", 8503)
    SERVER_4 = ("127.0.0.1", 8504)