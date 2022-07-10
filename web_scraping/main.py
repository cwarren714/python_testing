# https://jsonplaceholder.typicode.com/for easy api content
# scrapy.org for full web-scraping framework

import requests
from bs4 import BeautifulSoup
import pprint

pages = list(range(1, 4))
hn = []


def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda key: key['votes'], reverse=True)


def create_custom_hn(links, subtext):
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})


for p in pages:
    if p == 1:
        res = requests.get('https://news.ycombinator.com/news')
    elif p > 1:
        res = requests.get('https://news.ycombinator.com/news?p=' + str(p))
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.find_all(div='score'))
    # print(soup.prettify())
    links = soup.select('.titlelink')
    subtext = soup.select('.subtext')
    create_custom_hn(links, subtext)
sort_stories_by_votes(hn)

pprint.pprint(hn)
