# Web Scraping program that uses data from baitme.com and lists out all product names and prices of hats posted by
# the online vendor.

from bs4 import BeautifulSoup
import requests
#Requests from url and filtering out all hats
html_text = requests.get("https://www.baitme.com/headwear").text
soup = BeautifulSoup(html_text, "lxml")
hats = soup.find_all("li", class_='item last')

#Sorts through HTML Tags and creates variables corresponding from search
for hat in hats:
    product_name = hat.find("h2", class_="product-name").text
    price = hat.find("span", class_="price").text
    product_info = hat.div.h2.a["href"]

#Print statements for output
    print(f'Product Name: {product_name}')
    print(f'Price: {price}')
    print(f'Product Page: {product_info}')
    print(" ")