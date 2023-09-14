import requests

print(requests.__version__)

resp=requests.get("https://raw.githubusercontent.com/157123gf/404-lab1/master/untitled-1.py")

print(resp.text)