import requests

url = 'https://wttr.in/san%20francisco?nTqu&lang=en'
response = requests.get(url)


print(response.text)