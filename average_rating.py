import pandas as pd
import requests
from bs4 import BeautifulSoup

# open excel file where you want to store your data

data_file = pd.read_excel('engg_data.xlsx')

# using requests provide the url of the site which you want to scrape
request = requests.get("https://www.shiksha.com/engineering/colleges/b-tech-colleges-mumbai-all")

soup = BeautifulSoup(request.content, 'html.parser')

# find respective class of the tag which contains the data you want
patch = soup.find_all(class_="ctpv2-rating")

avg_rating = []
for i in range(len(patch)):
    avg_rating.append(patch[i].get_text())

avg_rating.insert(6, '-')
avg_rating.insert(21, '-')

# insert data in table
data_file["Average Rating"] = avg_rating

# to save file in excel
data_file.to_excel('engg_data.xlsx', index=False)
