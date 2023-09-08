import requests
from bs4 import BeautifulSoup

name = input("Enter Persons name: ")
link  = 'https://www.google.com/search?q=' + str(name) +" "+ "Wikipedia"
link  = link.replace(' ','+')
res = requests.get(link)

soup  = BeautifulSoup(res.text,"html.parser")

for sp in soup.find_all('div'):
    try:
        link = sp.find('a').get('href')  
        if('en.wikipedia.org' in link):
            break
    except:
        pass

link = (link[7:]).split('&')[0]
res = requests.get(link)
soup = BeautifulSoup(res.text, 'html.parser')
paragraphs = ' '
for p in soup.find_all('p'):
    paragraphs += p.text
    paragraphs += '\n'   
paragraphs = paragraphs.strip()

with open(name + ".txt" , 'w', encoding='utf-8') as fd:
    fd.write(paragraphs)
print("DONE")