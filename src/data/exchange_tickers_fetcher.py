from bs4 import BeautifulSoup
import json
import requests

STOCK_LIST_URL = "https://stockanalysis.com/stocks/"

def get_stock_list_html(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')

def get_stock_list_html_local(local_path):
    with open(local_path) as stock_list_html:
        return BeautifulSoup(stock_list_html, 'html.parser')
    
def get_listed_stocks(from_web=False):
    if from_web:
        stock_html_parser = get_stock_list_html(STOCK_LIST_URL)
    else:
        stock_html_parser = get_stock_list_html_local("src/data/stock_list.html")

    stock_table = stock_html_parser.body.find_all('a')
    stocks = [link.text for link in stock_table[1:] if link.get('href').startswith("https://stockanalysis.com/stocks/")]

    return stocks

    # with open('tickers.txt', 'w', newline='') as file:
    #     json.dump(stocks[1:-1], file)