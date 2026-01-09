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

    SERVER_1 = ("127.0.0.1", 8801)
    SERVER_2 = ("127.0.0.1", 8802)
    SERVER_3 = ("127.0.0.1", 8803)
    SERVER_4 = ("127.0.0.1", 8804)