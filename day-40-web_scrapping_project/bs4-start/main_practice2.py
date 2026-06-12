import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(class_="titleline")
articles_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.get_text()
    articles_texts.append(text)
    link = article_tag.find("a").get("href")
    articles_links.append(link)


article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]
#print(articles_texts)
#print(articles_links)
most_upvoted = max(article_upvotes)
index_of_most_upvoted = article_upvotes.index(most_upvoted)
print(articles[index_of_most_upvoted].get_text())
link = articles[index_of_most_upvoted].find("a").get("href")

print(link)
#title = [title.find_all(class_="titleline", name="span", class_="score") for title in article_upvotes if most_upvoted == soup.find_all(name="span", class_="score")]
#print(title)


#print(title.find_all(class_="titleline", name="span", class_="score"))



#titles = soup.find_all(name="span", class_="score")
#print(titles)
#upvoted_most_id = [title.get("id") for title in titles if int(title.get_text().split()[0]) == most_upvoted]
#print(index(upvoted_most_id))
#upvoted_most_title = soup.find(name="tr", id="upvoted_most_id")
#print(upvoted_most_title)
