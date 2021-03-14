from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.npr.org/?refresh=true').text
soup  = BeautifulSoup(source, 'lxml')

for titles in soup.find_all ('h3', class_='title'):
    CleanTitles = titles.text
    print (CleanTitles)