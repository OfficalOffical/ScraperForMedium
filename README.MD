# Medium scraper

This scraper pulls the image number, follower number, clap number, text inside the article, reading time, published date, and title from Medium archives. 

## Installation

All requirements are in the requirements text file. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements

## Usage

The program has two options Selenium for scraping one page with a scroll-down option. And the archive to scrape all data from the archive.

### Selenium
As you can see between lines 18 and 63 we have a selenium scraper it's commented out because we are not using it on this project but you can use it to scrape one page as it uses the scroll down option. you might need to change tags on the 49. line inside the soup.find_all()

### Archive (Main part)

This code can be used to pull archive data from Medium's tags. The Medium has an archive for each of his tags that you can find it by just adding /archive at the end of it. In our program, we are pulling data from ["Türkçe"](https://medium.com/tag/t%C3%BCrk%C3%A7e/archive) tag. You can put your own tag just by changing line 176's tag section. And also it pulls all the data from between the range of the for loop in line 168. I advise you to pull data separately since it might take a long and Medium might block your IP. So we have also csvMerger.py you can combine your CSV's in it.

![image](https://user-images.githubusercontent.com/18538179/182559371-53526064-425e-4298-accc-0484d266f97b.png)

# Usefull reminders

- For changing range -> Line 168 for loop
- For changing Tag -> Line 176 inside the request
- For changing to Selenium -> line 18-63 commented out. 
- For merging Csv -> use csvMerger.py

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
