
import requests
import csv
import pandas as pd
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup





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
    counter = 0
    print("Started scraping from Web archives")
    titleHolder = []
    dateHolder = []
    tagsHolder = []
    readingTimeHolder = []
    textIndexHolder = []
    clapHolder = []
    followerHolder = []
    numberOfImages = []

    print("This website contains :", len(webHolder), "pages")

    for pages in webHolder:
        counter +=1
        tempTextHolder = []

        try:
            page = requests.get(pages)
        except Exception as e:
            print("we got error ",counter)
            continue


        soup = BeautifulSoup(page.content, 'html.parser')

        img = soup.find_all('img',  class_="cf")

        date = soup.find_all('p', class_="pw-published-date")

        title = soup.find_all('h1', class_='pw-post-title')

        text = soup.find_all('p', class_='pw-post-body-paragraph')

        readinTime = soup.find_all('div', class_='pw-reading-time')

        try:
            clap, follower = aditionalValues(pages)
        except Exception as e:
            continue

        for texts in text:
            tempTextHolder.append(texts.get_text())


        if (title  and date  and readinTime ):
                titleHolder.append(title[0].get_text())
                dateHolder.append(date[0].get_text())
                readingTimeHolder.append(readinTime[0].get_text())
                textIndexHolder.append(tempTextHolder)
                clapHolder.append(clap)
                followerHolder.append(follower)
                numberOfImages.append(len(img))



    print("we have :", len(titleHolder), "pages in total")
    print("we have :", len(dateHolder), "data in total")
    print("we have :", len(readingTimeHolder), "reading in total")
    print("we have :", len(textIndexHolder), "text in total")
    print("we have :", len(clapHolder), "clap in total")
    print("we have :", len(followerHolder), "follower in total")
    print("we have :", len(numberOfImages), "number of image in total")


    header = ["Title", "Date", "Reading time", "Text", "Clap", "Follower", "Number of images"]

    with open('dataHolder.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(zip(titleHolder, dateHolder, readingTimeHolder, textIndexHolder, clapHolder, followerHolder, numberOfImages))
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

    for x in range(2009, 2015 + 1):


        print("Started scaping Websites from year : " + str(x))
        tempCounter = 0
        webRedirectingForMonth = []
        webRedirectingForDay = []

        page = requests.get("https://medium.com/tag/t%C3%BCrk%C3%A7e/archive/" + str(x))



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

    print("we have :", len(webHolder), "pages in total")
