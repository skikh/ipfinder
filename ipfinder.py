from bs4 import BeautifulSoup

with open("../ipfinder/index.html") as file:
    src = file.read()
print(src)