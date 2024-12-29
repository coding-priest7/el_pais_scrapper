import os
import re
import time
import requests
from bs4 import BeautifulSoup

def download_image(image_url, title):
    sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)  
    save_path = f"data/images/{sanitized_title}.jpg"  
    
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Image saved as: {save_path}")
    else:
        print(f"Failed to download image from {image_url}")


def fetch_and_download_cover_image(article, driver):

    driver.get(article["link"])
    time.sleep(5) 
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Locate the specific div containing the cover image
    cover_image_div = soup.find("div", class_="a_e_m")
    if cover_image_div:
        img_tag = cover_image_div.find("img")
        if img_tag and "srcset" in img_tag.attrs:
            srcset = img_tag["srcset"]
            cover_image_url = srcset.split(",")[0].split()[0] 

            sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', article['title'])
            image_path = f"data/images/{sanitized_title}.jpg"

            print(f"Downloading cover image for article: {article['title']}")
            download_image(cover_image_url, image_path)

            article["image_path"] = image_path
        else:
            print(f"No valid 'srcset' attribute found in the image tag for article: {article['title']}")
    else:
        print(f"Cover image div not found for article: {article['title']}")
