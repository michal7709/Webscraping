from bs4 import *
import lxml

# Tu możemy sobie otworzyć bo otwieramy lokalnie. Jednakże jak chcemy ściągnąć z sieci wtedy musimy użyć modułu requests
with open("Page.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# soup_b = soup.prettify()
# print(soup_b)
allh1 = soup.findAll("h1")

# h1 = soup.find("h1", class_ = "pierwszy")
# print(h1)
# print(h1.getText())
print(allh1)

csschoosing = soup.select(".pierwszy")
soup.select_one("h1")
print(csschoosing)