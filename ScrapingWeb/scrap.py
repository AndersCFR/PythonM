#we can add /robots.txt y te dice lo que puedes hacer scrapting en un sitio web
import requests
from bs4 import BeautifulSoup #this gives the chane to clean the HTML
import pprint

res = requests.get('https://news.ycombinator.com')
res2 = requests.get('https://news.ycombinator.com/news')

print(res)
#print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

#print(soup.body)
#print(soup.find_all('a'))
print(soup.find('a'))
#print(soup.select('.score'))
links = soup.select('.storylink')
links2 = soup.select('.storylink')

subtext = soup.select('.subtext')
subtext2 = soup.select('.subtext')

megalinks = links + links2
megasubtext = subtext + subtext2


def sort_stories(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)


def create_custom_hn(megalinks, megasubtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 85:
                    hn.append({'title': title, 'link': href, 'votes':points})
    return sort_stories(hn)

pprint.pprint(create_custom_hn(megalinks, megasubtext))


