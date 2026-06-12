import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
soup.prettify()

every_movie = [movie.get_text() for movie in soup.find_all(name="h3", class_="title")]
every_movie.reverse()

with open("movies.txt", "w") as file:
    for movie in every_movie:
        file.write(movie + "\n")
