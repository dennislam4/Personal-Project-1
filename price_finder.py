# Web Scraping program that uses data from baitme.com and lists out all product names and prices of hats posted by
# the online vendor.

from bs4 import BeautifulSoup
import requests
import re
import time

#Requests from url and filtering out all hats.
html_text = requests.get("https://www.baitme.com/headwear").text
soup = BeautifulSoup(html_text, "lxml")
hats = soup.find_all("li", class_ = 'item last')

def price_finder():
    """
    Webscraper that scrapes baitme.com and lists out product name, color and prices of hats.
    """
    for hat in hats:
     # Sorts through HTML Tags and creates variables corresponding from search.
        product_name = hat.find("h2", class_ = "product-name").text
        product_name = re.sub("\(.*?\)","()", product_name).replace("()","")
        price = hat.find("span", class_ = "price").text
        product_info = hat.div.h2.a["href"]
        product_color = hat.find("h2", class_ = "product-name").text
        product_color = re.search('\(([^)]+)', product_color).group(1)

    #Print statements for output
        print(f'Product Name: {product_name}')
        print(f'Product Color: {product_color.title()} ')
        print(f'Price: {price}')
        print(f'Product Page: {product_info}')
        print(" ")

if __name__ == "__main__":
    #Runs the function every hour.
    while True:
        price_finder()
        time.sleep(3600)
