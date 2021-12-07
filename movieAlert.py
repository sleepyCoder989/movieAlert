from bs4 import BeautifulSoup
import requests
import re
import config


def sendAlert(msg):
    response = requests.get(msg)
    return response.json()

url = "https://in.bookmyshow.com/explore/movies-nagpur"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

regex = re.compile(r".*gBgfCW.*")

movies = soup.find_all("div", {"class": regex})

searchMovie = "Spider-Man: No Way Home"

telegramBot = "https://api.telegram.org/bot" + config.token + "/sendMessage?chat_id="

chatIds = ["863040321", "963147207"]

for movie in movies:
    if movie.get_text() == searchMovie:
        for chatId in chatIds:
            print(sendAlert(
                telegramBot
                + chatId
                + "&parse_mode=Markdown&text=Tickets Available for "
                + searchMovie                
            ))
