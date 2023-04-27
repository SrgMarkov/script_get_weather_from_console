import requests


def get_weather(loc):
    url_template = 'https://wttr.in/{}?n?q?M?m?T'
    lang = {'lang': 'ru'}
    url = url_template.format(loc)
    response = requests.get(url, params=lang)
    return response.text


location_list = ['London', 'cvo', 'Череповец']

for location in location_list:
    print(get_weather(location))
    