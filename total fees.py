import pandas as pd
import requests
from bs4 import BeautifulSoup

# open excel file where you want to store your data
data_file = pd.read_excel('engg_data.xlsx')

# using requests provide the url of the site which you want to scrape
request = requests.get("https://www.shiksha.com/engineering/colleges/b-tech-colleges-mumbai-all")

soup = BeautifulSoup(request.content, 'html.parser')

# find respective class of the tag which contains the data you want
patch = soup.find_all(class_="shadowCard ctpCard")

detail_list = []
for i in range(len(patch)):
    detail_list.append(patch[i].find_all(class_="flexRowEqual")[1])

fees = []
for i in range(len(detail_list)):
    fees.append(detail_list[i].get_text()[10:][3:6])

for i in range(len(fees)):
    if fees[i] == 'dia':
        fees[i] = '-'
    elif fees[i] == '6 L':
        fees[i] = '6'
    else:
        continue

# insert data in table
data_file["Total Fees"] = fees
# data_file.to_excel('engg_data.xlsx',index=False)
