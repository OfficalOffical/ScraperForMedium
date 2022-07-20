import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def mainWebScraper():
    scrapeWeb()


def scrapeWeb():
# Create a new instance of the Firefox driver.

    driver = webdriver.Chrome()

    # Open the URL
    driver.get("https://medium.com/tag/t%C3%BCrk%C3%A7e")


    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the source code of the page

    soup = BeautifulSoup(driver.page_source, "html.parser")


    # Find all the <a> tags
    links = soup.find_all('a', class_='au av aw ax ay az ba bb bc bd be bf bg bh bi')

    for link in links:
        if(link.get('aria-label') != None):
            print(link.get('href'))







