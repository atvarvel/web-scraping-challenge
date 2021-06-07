import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape():

    mars_data = {}

    # Setup splinter
    executable_path = {'executable_path': 'C:/Users/atvar/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    browser.quit()

    # Setup splinter
    executable_path = {'executable_path': 'C:/Users/atvar/.wdm/drivers/chromedriver/win32/91.0.4472.19/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image = soup.find('img', class_='headerimage fade-in')
    image_src = featured_image['src']

    featured_image_url = f'https://spaceimages-mars.com/{image_src}'

    browser.quit()

    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)

    mars_df = tables[1]

    mars_table_html = mars_df.to_html()
    mars_table_html = mars_table_html.replace('\n', '')

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"}
    ]

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image": featured_image_url,
        "table": mars_table_html,
        "hemispheres": hemisphere_image_urls
    }

    return mars_data