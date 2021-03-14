from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.npr.org/').text
print(source)