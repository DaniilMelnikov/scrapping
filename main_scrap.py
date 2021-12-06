import requests

from bs4 import BeautifulSoup

from pprint import pprint

import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

resp = requests.get('https://habr.com/ru/all/')
resp.raise_for_status()

def print_list(string):
    for word in KEYWORDS:
        if word in string:
            print(f'{data[0]}, {header.text}, {href}')

soup = BeautifulSoup(resp.text, 'html.parser')
articles = soup.find_all('article')
for article in articles:
    time = str(article.find('time'))
    data = re.search('\d+\-\d+\-\d+', time)
    header = article.find('h2')
    snippet_v1 = article.find('div', class_='article-formatted-body article-formatted-body_version-1')
    snippet_v2 = article.find('div', class_='article-formatted-body article-formatted-body_version-2')
    href = header.find('a')
    reg_href = re.search('\"\/\w+\/\w+\/.+\/\"', str(href))
    href = re.sub('\"(\/\w+\/\w+\/.+\/)\"', 'https://habr.com\\1', reg_href[0])

    print_list(str(snippet_v1))
    print_list(str(snippet_v2))


    