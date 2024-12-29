from bs4 import BeautifulSoup
import time
import requests

BASE_URL = "https://elpais.com/"

def get_opinion_articles(driver):
    url = f"{BASE_URL}opinion/"
    driver.get(url)
    time.sleep(5) 

    soup = BeautifulSoup(driver.page_source, "html.parser")

    articles = []
    for article in soup.select("article.c header.c_h h2.c_t a")[:5]:
        title = article.text.strip()
        link = article["href"]
        if not link.startswith("http"):
            link = BASE_URL + link.lstrip("/")

        content = get_article_content(link, driver)  # Pass the driver to the content scraper
        articles.append({"title": title, "link": link, "content": content})
    
    return articles

def get_article_content(url, driver):
    driver.get(url)
    time.sleep(5) 

    soup = BeautifulSoup(driver.page_source, "html.parser")
    paragraphs = soup.find_all('p')
    
    figcaption_spans = soup.select('figcaption span:not(.a_m_m)')
    
    content = " ".join(tag.text for tag in paragraphs) + " " + " ".join(span.text for span in figcaption_spans)
    return content.strip()
