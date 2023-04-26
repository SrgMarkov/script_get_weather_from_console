import requests

url_template = 'https://wttr.in/{}?n?q?M?m?T'

loc = input('Input location: ')
lang = {'lang': 'ru'}
url = url_template.format(loc)
response = requests.get(url, params=lang)

print(response.text)