import requests

# url = 'https://wttr.in/san%20francisco?nTqu&lang=en'

url_template = 'https://wttr.in/{}'

article_id = input('Input location: ')
url = url_template.format(article_id)
response = requests.get(url)

print(response.text)