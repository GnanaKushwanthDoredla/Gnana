from urllib import request
from bs4 import BeautifulSoup
url = input("Enter")
position = int(input("Enter position"))
count = int(input("Enter count"))
for i in range(count):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup("a")
    s = []
    t = []
    for tag in tags:
        x = tag.get('href',None)
        s.append(x)
        y = tag.text
        t.append(y)
    print(t[position-1])
    url = s[position-1]

