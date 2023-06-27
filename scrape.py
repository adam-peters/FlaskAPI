from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.walkscore.com/cities-and-neighborhoods/').text
soup = BeautifulSoup(html_text, 'lxml')

block = soup.find_all('div', class_='mag-block')[1]

titles = block.find_all('h2')

for title in titles:
    print(title.text)
