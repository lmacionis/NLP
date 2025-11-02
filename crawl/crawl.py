import requests
from lxml.etree import HTML
from lxml import etree
from requests import HTTPError
import pandas as pd
import numpy as np


URL = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"


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
            file.close()

        return html

    # Get links and titles for tutorials from web page.
    def get_link_title(self):
        tree = HTML(self.load_data())   # str
        links = tree.xpath('//div[@class="text"]//a/@href') # returns dtype list
        titles = tree.xpath('//div[@class="text"]//a/span')
        titles_text = [title.text for title in titles]
        
        return links, titles_text

    def text(self):
        tree = HTML(self.load_data())   # str
        info = tree.xpath('//div[@class="text"]//span/text() | //div[@class="text"]//strong/text() | //div[@class="text"]//a/@href')

        return info


get_data = Crawl(URL).get_data()

# get_link_title = Crawl(URL).get_link_title()

# Take titles and URL'S and form csv file.
link, title = Crawl(URL).get_link_title()
def save_as_csv(link, title):
    if len(title) != len(link):
        # Adding NaN to fix diference between link's and titles, that we could transform it into DataFrame. 
        title.extend(["NaN"] * (len(link) - len(title)))
        dict_for_csv = {"Title": title, "Link": link}
    
    df = pd.DataFrame(dict_for_csv)    
    df.index += 1
    df.to_csv("./data/data_as.csv")

save_as_csv(link, title)
