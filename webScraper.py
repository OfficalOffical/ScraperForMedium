import time
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json


def mainWebScraper():
    scrapeWeb()


def scrapeWeb():
    # Create a new instance of the Firefox driver.
    tempCounter = 0
    webHolder = []

    driver = webdriver.Chrome()

    # Open the URL
    driver.get("https://medium.com/tag/t%C3%BCrk%C3%A7e")

    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    """while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height"""

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all the <a> tags
    links = soup.find_all('a', class_='au av aw ax ay az ba bb bc bd be bf bg bh bi')

    for link in links:
        if (link.get('aria-label') != None):
            tempCounter += 1
            if (tempCounter % 3 == 0):
                print(link.get('href'))
                webHolder.append("https://medium.com" + link.get('href'))

    # Close the browser
    driver.quit()

    print(len(links))

    pullDataFromWeb(webHolder)


def pullDataFromWeb(webHolder):

    for pages in webHolder:
        print(pages)
        #request with incognito mode
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        page = requests.get(pages, headers=headers, cookies={"over18": "1", "incognito": "1"})


        clap, follower = aditionalValues(pages)



        soup = BeautifulSoup(page.content, 'html.parser')

        text = soup.find_all('p', class_='pw-post-body-paragraph')



        for texts in text:
            print(texts.get_text())
            # Prints the text of the paragraph
        print(clap, follower)
        print("//////////////////////////////////////////////////////////////////////////////////////////////")


def aditionalValues(page):
    aditionalPage = requests.get(page).content.decode("utf-8")

    claps = aditionalPage.split("clapCount\":")[1]
    endIndex = claps.index(",")
    claps = int(claps[0:endIndex])

    follower = aditionalPage.split("followerCount\":")[1]
    followerIndex = follower.index(",")
    followerNumber = int(follower[0:followerIndex])

    return claps, followerNumber
