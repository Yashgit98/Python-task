import requests as rq
from bs4 import BeautifulSoup

def fetch_html(url):
    resp = rq.get(url)
    return BeautifulSoup(resp.content, 'html.parser')

def get_usd_market_price(Currency):
    url = "https://www.google.com/finance/quote/USD-INR"
    bsoup = fetch_html(url)
    exchange_rate_div = bsoup.find("div", attrs={'data-last-price': True})
    if exchange_rate_div:
        return float(exchange_rate_div['data-last-price'])
    raise ValueError("USD to INR exchange rate not found.")

def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    bsoup = fetch_html(url)
    price_div = bsoup.find("div", attrs={'data-last-price': True})
    if price_div:
        price = float(price_div['data-last-price'])
        currency = price_div['data-currency-code']
        usd_price = round(get_usd_market_price(currency),2)
        inr_price = round(usd_price * get_usd_market_price(currency),2)

        return {
            'stock_name' : ticker,
            'exchange' : exchange,
            'currency' : currency,
            'USD_Price' : usd_price,
            'INR_Price' : inr_price
        }
    raise ValueError(f"Price information for {ticker} on {exchange} not found.")
ticker = 'GOOG'
exchange = 'NASDAQ'
print(get_price_information(ticker,exchange))