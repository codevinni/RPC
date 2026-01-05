from rpc_server import RPCServer

s3 = RPCServer(ip="127.0.0.1", port=8503, cacheFilename="s3_cache.json", maxCacheSize=10000, 
               allowedOps=["soma", "subtracao", "multiplicacao", "divisao", "fatorial", "uolNews", "primes"])

print("\nS3 iniciado na porta 8503\n")
s3.run()