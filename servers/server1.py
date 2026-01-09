from rpc_server import RPCServer

if __name__ == "__main__":
    
    s1 = RPCServer(ip="0.0.0.0", port=8801, cacheFilename="s1_cache.json", maxCacheSize=10000, 
                   allowedOps=["soma", "subtracao", "multiplicacao", "divisao", "fatorial"])

    print(f"\nS1 iniciado em {s1.ip}:{s1.port}\n")
    s1.run()