import requests


def weather(loc):
    url_template = 'https://wttr.in/{}?n?q?M?m?T'
    lang = {'lang': 'ru'}
    url = url_template.format(loc)
    response = requests.get(url, params=lang)
    return response.text


print(weather('London'))
print(weather('cvo'))
print(weather('Череповец'))
