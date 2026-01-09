from rpc_server import RPCServer

if __name__ == "__main__":
    
    s2 = RPCServer(ip="0.0.0.0", port=8802, cacheFilename="s2_cache.json", maxCacheSize=10000, 
                   allowedOps=["soma", "subtracao", "multiplicacao", "divisao", "fatorial"])

    print(f"\nS2 iniciado em {s2.ip}:{s2.port}\n")
    s2.run()