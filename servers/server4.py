from rpc_server import RPCServer

if __name__ == "__main__":
    
    s4 = RPCServer(ip="0.0.0.0", port=8804, cacheFilename="s4_cache.json", maxCacheSize=10000, 
                   allowedOps=["primes", "mathSolverAi"])

    print(f"\nS4 iniciado em {s4.ip}:{s4.port}\n")
    s4.run()