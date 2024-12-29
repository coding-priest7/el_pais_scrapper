from scraper.article_scraper import get_opinion_articles, get_article_content
from scraper.image_downloader import fetch_and_download_cover_image, download_image
from scraper.translator import translate_titles
from collections import Counter
import re
import time

from config.api_keys import username, access_key  
from tests.browserstack_tests import initialize_browserstack_driver 

def main():
    # Initialize BrowserStack driver
    driver = initialize_browserstack_driver(username, access_key)
    print("Fetching articles...")

    # Open El País opinion section in BrowserStack browser
    driver.get("https://elpais.com/opinion/")
    time.sleep(5)

    # Fetch opinion articles
    articles = get_opinion_articles(driver)  # Pass the driver to the scraper

    for i, article in enumerate(articles):
        print(f"\nFetching content for: {article['title']}")
        content = get_article_content(article["link"], driver)  # Pass the driver to the content scraper
        articles[i]["content"] = content

        # Print the title and content
        print(f"Title: {article['title']}")
        print(f"Content: {content}\n")

        # Fetch and download the cover image
        fetch_and_download_cover_image(article, driver)

    translated_titles = []

    print("\nTranslating titles...")
    titles = [article["title"] for article in articles]
    translated_titles = translate_titles(titles)

    print("\nTranslated Titles:")
    for title in translated_titles:
        print(title)

    print("\nAnalyzing translated titles...")
    word_counts = Counter(re.findall(r"\w+", " ".join(translated_titles).lower()))
    print("Word counts:", word_counts)  

    repeated_words = {word: count for word, count in word_counts.items() if count > 2}
    print("Repeated words:", repeated_words)

    driver.quit()

if __name__ == "__main__":
    main()
