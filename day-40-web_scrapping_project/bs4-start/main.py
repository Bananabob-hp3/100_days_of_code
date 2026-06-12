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
most_upvoted = max(article_upvotes)

index_of_most_upvoted = article_upvotes.index(most_upvoted)

title_of_most_upvoted = articles_texts[index_of_most_upvoted]
link_of_most_upvoted = articles_links[index_of_most_upvoted]
print(title_of_most_upvoted)
print(link_of_most_upvoted)

