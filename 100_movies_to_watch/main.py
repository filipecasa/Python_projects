import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
# print(soup.text)

movies_name = soup.find_all("h3", class_="title")
movies_list = [movie.getText() for movie in movies_name]
# print(movies_list[::-1])
# movies_1_to_100 = [movies_list[n] for n in range(len(movies_list) -1, -1, -1)]
# print(movies_1_to_100)
movies_list.reverse()
print(movies_list)

with open("movies.txt", mode="w") as file:
    for movie in movies_list:
        file.writelines(f"{movie}\n")

