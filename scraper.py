import requests #accessing URL and pull out he actual data
from bs4 import BeautifulSoup #parse and pulls individual items from it

URL = 'https://www.amazon.in/Sony-PS5-PlayStation-Console/dp/B0BRCP72X8/ref=sr_1_3?crid=23EEQBEN6FQ3H&keywords=ps5&qid=1707545306&sprefix=ps%2Caps%2C230&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
#gives information about browser

page = requests.get(URL, headers=headers)
#returns all the data from the website

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="corePriceDisplay_desktop_feature_div").get_text() #need to fix this
#cant compare string to number so converting
converted_price = price[0:5]


print(converted_price)