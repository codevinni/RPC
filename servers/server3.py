from rpc_server import RPCServer

if __name__ == "__main__":
    
    s3 = RPCServer(ip="0.0.0.0", port=8803, cacheFilename="s3_cache.json", maxCacheSize=10000, 
                   allowedOps=["uolNews", "primes"])

    print(f"\nS3 iniciado em {s3.ip}:{s3.port}\n")
    s3.run()