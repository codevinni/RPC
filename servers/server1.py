from rpc_server import RPCServer

s1 = RPCServer(ip="127.0.0.1", port=8501, cacheFilename="s1_cache.json", maxCacheSize=10000, 
               allowedOps=["soma", "subtracao", "multiplicacao", "divisao", "fatorial", "uolNews", "primes"])

print("\nS1 iniciado na porta 8501\n")
s1.run()