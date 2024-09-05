Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import psutil
... import platform
... 
... def get_system_info():
...     print(f"System: {platform.system()}")
...     print(f"Node Name: {platform.node()}")
...     print(f"Release: {platform.release()}")
...     print(f"Version: {platform.version()}")
...     print(f"Machine: {platform.machine()}")
...     print(f"Processor: {platform.processor()}")
...     print(f"CPU Usage: {psutil.cpu_percent()}%")
...     print(f"Memory Usage: {psutil.virtual_memory().percent}%")
...     print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
... 
... if __name__ == "__main__":
...     get_system_info()
