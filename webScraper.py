import time
import requests
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json





def mainWebScraper():

    temp2 = scrapeWebFromArchive()


"""def scrapeWeb():
    # Create a new instance of the Firefox driver.
    tempCounter = 0
    webHolder = []

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

    pullDataFromWeb(webHolder)"""


def pullDataFromWeb(webHolder):

    textIndexHolder = []
    clapHolder = []
    followerHolder = []

    for pages in webHolder:
        tempTextHolder = []



        page = requests.get(pages)

        clap, follower = aditionalValues(pages)

        soup = BeautifulSoup(page.content, 'html.parser')

        text = soup.find_all('p', class_='pw-post-body-paragraph')

        for texts in text:
            tempTextHolder.append(texts.get_text())



        textIndexHolder.append(tempTextHolder)
        clapHolder.append(clap)
        followerHolder.append(follower)

    header = ["Clap", "Follower", "Text"]

    with open('dataHolder.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(zip(clapHolder, followerHolder, textIndexHolder))
    f.close()

    data = pd.read_csv('dataHolder.csv')
    print(data.head())






def aditionalValues(page):
    aditionalPage = requests.get(page).content.decode("utf-8")

    claps = aditionalPage.split("clapCount\":")[1]
    endIndex = claps.index(",")
    claps = int(claps[0:endIndex])

    follower = aditionalPage.split("followerCount\":")[1]
    followerIndex = follower.index(",")
    followerNumber = int(follower[0:followerIndex])

    return claps, followerNumber

def scrapeWebFromArchive():

    tempCounter = 0
    webHolder = []
    webRedirectingForMonth = []
    webRedirectingForDay = []
    page = requests.get("https://medium.com/tag/t%C3%BCrk%C3%A7e/archive/2015")
    soup = BeautifulSoup(page.content, 'html.parser')




    links = soup.find_all('a', class_ = "")



    for x in range(2009,2011):
        print("Finished year: " + str(x))
        tempCounter = 0
        webRedirectingForMonth = []
        webRedirectingForDay = []

        page = requests.get("https://medium.com/tag/t%C3%BCrk%C3%A7e/archive/"+str(x))
        soup = BeautifulSoup(page.content, 'html.parser')

        links = soup.find_all('a', class_="")
        for link in links:
            if (link.get('data-action-source') != None):
                webHolder.append(link.get('href'))
            else:
                webRedirectingForMonth.append(link.get('href'))

        for link in webRedirectingForMonth:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            links = soup.find_all('a', class_="")
            for link in links:
                if (link.get('data-action-source') != None):
                    webHolder.append(link.get('href'))
                else:
                    webRedirectingForDay.append(link.get('href'))

        for link in webRedirectingForDay:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            links = soup.find_all('a', class_="")
            for link in links:
                if (link.get('data-action-source') != None):
                    webHolder.append(link.get('href'))


    pullDataFromWeb(webHolder)

    print("we have :",len(webHolder),"pages in total")







