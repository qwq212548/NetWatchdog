import socket
import subprocess
import time

def ping_host(host, count=4, timeout=2):
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), "-W", str(timeout), host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0, result.stdout
    except Exception as e:
        return False, str(e)

def check_port(host, port, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

def dns_lookup(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as e:
        return None
