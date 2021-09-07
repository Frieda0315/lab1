import requests

response = requests.get('http://google.com/')

print('Your IP is {0}'.format(response.json()['origin']))
