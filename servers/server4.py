from rpc_server import RPCServer

s4 = RPCServer(ip="127.0.0.1", port=8504, cacheFilename="s4_cache.json", maxCacheSize=10000, 
               allowedOps=["soma", "subtracao", "multiplicacao", "divisao", "fatorial", "uolNews", "primes", "mathSolverAi"])

print("\nS4 iniciado na porta 8504\n")
s4.run()