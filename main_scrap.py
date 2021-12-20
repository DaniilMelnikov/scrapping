import requests

from bs4 import BeautifulSoup

import re

KEYWORDS = ['дизайн', 'фото', 'API', 'Python', 'CEO', 'ML', 'HR', 'PHP']

resp = requests.get('https://habr.com/ru/all/')
resp.raise_for_status()

def print_list(string):
    result = re.sub(r'(\<)\/*(\w+\s*\S*\w+\s*\S*)(\>)', '', string, 0, re.MULTILINE)
    for word in KEYWORDS:
        search_word = re.findall(word, result)
        if len(search_word) > 0:
            print(f'{data[0]}, {header.text}, {href}')

soup = BeautifulSoup(resp.text, 'html.parser')
articles = soup.find_all('article')
for article in articles:
    time = str(article.find('time'))
    data = re.search('\d+\-\d+\-\d+', time)
    header = article.find('h2')
    href = header.find('a')
    reg_href = re.search('\"\/\w+\/\w+\/.+\/\"', str(href))
    href = re.sub('\"(\/\w+\/\w+\/.+\/)\"', 'https://habr.com\\1', reg_href[0])
    text = article.find(class_='article-formatted-body article-formatted-body_version-1')
    if text == None:
        text = article.find(class_='article-formatted-body article-formatted-body_version-2')
        if text != None:
            print_list(str(text))
    else:
        print_list(str(text))