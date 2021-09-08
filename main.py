import requests

response = requests.get('http://google.com/')

print('Your IP is {0}'.format(response.json()['origin']))

pythonS = requests.get("https://raw.githubusercontent.com/Frieda0315/lab1/master/main.py")
print(pythonS.text)
