import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_news = response.text

soup = BeautifulSoup(yc_news, 'html.parser')
articles = soup.find_all(name="a", class_="titlelink")
article_titles = [tag.getText() for tag in articles]
article_links = [tag.get('href') for tag in articles]
article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name="span", class_="score")]
max_score = max(article_upvotes)
max_index = article_upvotes.index(max_score)
print(article_titles[max_index])
print(article_links[max_index])

