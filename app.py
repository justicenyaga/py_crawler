import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary")

print("Title: Votes")
for question in questions:
    # print("Title: ", question.select_one(".s-link").getText())
    # print("Votes: ", question.select_one(".s-post-summary--stats-item-number").getText())
    print(f"{question.select_one('.s-link').getText()}: {question.select_one('.s-post-summary--stats-item-number').getText()}")