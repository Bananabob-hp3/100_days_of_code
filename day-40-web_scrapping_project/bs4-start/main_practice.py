from bs4 import BeautifulSoup


with open("website.html") as file:
     contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.li)
#print(soup.prettify())
#print(soup.find_all("li")) #gives us First anchor tag
#print(soup.title.string)

#print(soup.li)


#print(soup.a)






























with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup)
all_anchor_tags = soup.find_all("a")
all_para_tags = soup.find_all("p")

for tag in all_anchor_tags:
 #   print(tag.get_text())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.string)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
