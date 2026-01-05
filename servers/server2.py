from rpc_server import RPCServer

s2 = RPCServer(ip="127.0.0.1", port=8502, cacheFilename="s2_cache.json", maxCacheSize=10000, 
               allowedOps=["soma", "subtracao", "multiplicacao", "divisao", "fatorial", "uolNews", "primes"])

print("\nS2 iniciado na porta 8502\n")
s2.run()