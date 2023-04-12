from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('div', {'id':'content'}).get_text())
# for sibling in bs.findAll('', {'class':'gift'}):
#     print(sibling.get_text())
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling.get_text())
