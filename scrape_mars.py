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
    mars_df.columns = ["Description", "Value"]
    mars_df = mars_df.set_index("Description")

    mars_table_html = mars_df.to_html()

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}
    ]

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image": featured_image_url,
        "table": mars_table_html,
        "hemispheres": hemisphere_image_urls
    }

    return mars_data