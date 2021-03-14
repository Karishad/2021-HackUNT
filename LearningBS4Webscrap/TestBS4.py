# Kieron Yin
# 3/13/2021
# A basic webscraper to grab titles from the NPR website
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.npr.org/').text
soup = BeautifulSoup(source, 'lxml')
for titles in soup.find_all('h3', class_='title'):
    cleanTitle = titles.text
    print(cleanTitle)