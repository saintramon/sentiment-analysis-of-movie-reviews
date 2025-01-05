import pandas as pd
import requests as req
from bs4 import BeautifulSoup

URL = 'https://letterboxd.com/film/anora/reviews/by/activity/page/'

review_list = [];

def scrape_reviews(page_url):
    response = req.get(page_url)


    if response.status_code != 200:
        print("FAILED FETCHING THE PAGE")
        return
    

    soup = BeautifulSoup(response.text, 'html.parser')

    review_elements = soup.find_all("li", class_="film-detail")

    for review in review_elements:
        try:
            text_review = review.find("div", class_="body-text -prose collapsible-text").find('p').get_text(strip=True)
            review_list.append(text_review)
        except AttributeError:
            continue



