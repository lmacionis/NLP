import requests
from lxml.etree import HTML
from lxml import etree
from requests import HTTPError


URL = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"


class Links:
    def __init__(self, source):
        self.source = source

    def get_link(self):
        response = requests.get(self.source)

        if response.status_code == 200:
            try:
                text = response.text
                assert isinstance(text, str)

                tree = HTML(text)
                links = tree.xpath('//div[@class="text"]//a[1]/@href') # returns dtype list

                return links

            except Exception as error:
                raise TypeError(f"Wrong data type: {error}")
        else:
            raise HTTPError(f"Page is unreachable: {response.status_code}")


get_link = Links(URL).get_link()
print(get_link)

# file = open("crawl/ex.txt", "w")
# file.write(resp.text)
# file.close()
