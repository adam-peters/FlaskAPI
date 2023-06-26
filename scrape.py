from bs4 import BeautifulSoup

with open('./templates/hello.html', 'r') as html_file:
    content = html_file.read();
   
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h2') # soup.find_all('div', class_='card')
    for tag in tags:
        print(tag.text)
