import os
from crawl.crawl2  import Crawl
import pandas as pd


URL = "https://www.w3schools.com/python/default.asp"
directory = "data"

# Creating directory for data storage.
def create_dir_data():
    try:
        os.mkdir(directory)
        print(f"Directory {directory} created successfully.")
    except FileExistsError:
        print(f"Directory {directory} already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

create_dir_data()


# Saving extracted links, as csv.
def save_as_csv(link, title):
    # dict_for_csv = {}

    if len(title) != len(link):
        # Adding NaN to fix diference between link's and titles, that we could transform it into DataFrame. 
        title.extend(["NaN"] * (len(link) - len(title)))
        dict_for_csv = {"Title": title, "Link": link}
    else:
        dict_for_csv = {"Title": title, "Link": link}

    df = pd.DataFrame(dict_for_csv)    
    df.index += 1
    df.to_csv("./data/data_as.csv")


# Extracting data.
Crawl(URL).get_data()
link, title = Crawl(URL).get_link_title()
save_as_csv(link, title)