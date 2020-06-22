from urllib import request
import xml.etree.ElementTree as ET
url = input("Enter")
connect = request.urlopen(url).read()
tree = ET.fromstring(connect)
counts = tree.findall("comments/comment/count")
sum = 0
for i in counts:
    sum = sum + int(i.text)
print(sum)

