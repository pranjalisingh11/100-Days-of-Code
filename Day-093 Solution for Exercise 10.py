import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-27&sortBy=publishedAt&apiKey=a1a54dd0cb664aeabd1579154e01d605"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------")