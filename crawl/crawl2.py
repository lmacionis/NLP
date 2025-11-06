import requests
from lxml.etree import HTML
from lxml import etree
from requests import HTTPError
import pandas as pd
import numpy as np


# URL = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"
URL = "https://www.w3schools.com/python/default.asp"
url_path = "https://www.w3schools.com/python/"


class Crawl:
    def __init__(self, source):
        self.source = source

    # Extracting html data from web page and saving to txt file.
    def get_data(self):
        response = requests.get(self.source)

        if response.status_code == 200:
            try:
                text = response.text
                assert isinstance(text, str)
                with open("./data/html_data.txt", "w") as file:
                    file.write(text)
                    file.close()

            except Exception as error:
                raise TypeError(f"Wrong data type: {error}")
        else:
            raise HTTPError(f"Page is unreachable: {response.status_code}")

    # Open data from html_data.txt file
    def load_data(self):
        path = "./data/html_data.txt"
        with open(path, "r") as file:
            html = file.read()

        return html

    # Get links and titles for tutorials from web page.
    def get_link_title(self):
        tree = HTML(self.load_data())   # str
        links = tree.xpath('//div[@id="leftmenuinnerinner"]//a/@href') # returns dtype list
        titles = tree.xpath('//div[@id="leftmenuinnerinner"]//a')
        titles_text = [title.text for title in titles]
        
        return links, titles_text

    def text(self):
        tree = HTML(self.load_data())   # str
        info = tree.xpath('//div[@id="main"]/h1/text() | \
                            //div[@id="main"]//span/text() | \
                            //div[@id="main"]//h2/text() | \
                            //div[@id="main"]//p/text() | \
                            //div[@id="main"]//div[@class="w3-code notranslate w3-black"]/text() | \
                            //div[@id="main"]//div[@class="w3-code notranslate w3-black"]/em/text() | \
                            //div[@id="main"]//h3/text() | \
                            //div[@class="w3-code notranslate pythonHigh"]/text() | \
                            //div[@class="w3-code notranslate pythonHigh w3-border-red"]/text() | \
                            //div[@id="main"]//code/text()')
        return info


get_data = Crawl(URL).get_data()

# get_link_title = Crawl(URL).get_link_title()

# Take titles and URL'S and form csv file.
link, title = Crawl(URL).get_link_title()
URL = url_path + link[10]
get_data = Crawl(URL).get_data()
print(URL)
info = Crawl(URL).text()
info = ' '.join(info)
print(info)