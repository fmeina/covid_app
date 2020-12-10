import urllib.request
from bs4 import BeautifulSoup


url = 'https://www.gov.pl/web/coronavirus/temporary-limitations/'


request = urllib.request.Request(url)
content = urllib.request.urlopen(request)

parse = BeautifulSoup(content, 'html.parser')

text1 = parse.find_all('article')


