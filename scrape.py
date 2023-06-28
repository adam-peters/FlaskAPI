from bs4 import BeautifulSoup
import requests

# city = input("Name a City in California: ")
city = "Riverside"

html_text = requests.get('https://www.walkscore.com/CA/' + city).text
soup = BeautifulSoup(html_text, 'lxml')

scores = soup.find_all('img')

for score in scores:
    print(score)
