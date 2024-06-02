import requests as rq
from bs4 import BeautifulSoup

def feath_html(url):
    # Fetch HTML content from URL
    resp = rq.get(url)
    return BeautifulSoup(resp.content, 'html.parser')

def get_usd_market_price(currency):
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    bsoup = feath_html(url)
    exchange_rate_div = bsoup.find("div", attrs={'data-last-price': True})
    
    if exchange_rate_div:
        return float(exchange_rate_div['data-last-price'])
    raise ValueError(f'Exchange rate for {currency} not fount.')

def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    bSoup =feath_html(url)
    price_div = bSoup.find('div', attrs={'data-last-price': True})
    if price_div:
        price = float(price_div['data-last-price'])
        currency = price_div['data-currency-code']
        usd_price = price if currency == 'USD' else round(price * get_usd_market_price(currency),2)
        return{
            'stock_name' : ticker,
            'exchange' : exchange,
            'INR_Price' : price,
            'currency' : currency,
            'USD_price' : usd_price
        }
    raise ValueError(f"Price information for {ticker} on {exchange} not found.")

ticker1 = 'TCS'
exchange1 = 'NSE'
ticker2 = 'M&M'
exchange2 = 'NSE'

print(get_price_information(ticker1,exchange1))
print()
print(get_price_information(ticker2,exchange2))

ticker3 = 'GOOG'
exchange3 = 'NASDAQ'

print(get_price_information(ticker3,exchange3))