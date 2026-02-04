import yfinance as yf

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="max").reset_index()
    return data
