import subprocess
import sys

servers = [
    "server1.py",
    "server2.py",
    "server3.py",
    "server4.py",
    "name_server.py"
]

processes = []

for s in servers:
    p = subprocess.Popen([sys.executable, s])
    processes.append(p)

for p in processes:
    p.wait()