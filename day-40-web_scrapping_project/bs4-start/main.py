from bs4 import BeautifulSoup


with open("website.html") as file:
     contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.li)
#print(soup.prettify())
print(soup.find_all("li").string) #gives us First anchor tag
#print(soup.title.string)
