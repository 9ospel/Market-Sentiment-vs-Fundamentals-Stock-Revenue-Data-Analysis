import matplotlib.pyplot as plt
import pandas as pd

def make_graph(stock_data, revenue_data, stock_name):

    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    revenue_data['Date'] = pd.to_datetime(revenue_data['Date'])

    stock_spec = stock_data[stock_data.Date <= '2021-06-14']
    rev_spec = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    ax1.plot(stock_spec.Date, stock_spec.Close.astype(float))
    ax1.set_title(f"{stock_name} Share Price")
    ax1.set_ylabel("Price ($US)")

    ax2.plot(rev_spec.Date, rev_spec.Revenue.astype(float))
    ax2.set_title(f"{stock_name} Revenue")
    ax2.set_ylabel("Revenue ($US Millions)")
    ax2.set_xlabel("Date")

    plt.tight_layout()
    plt.show()
