import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_revenue(url, table_title):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table')
    target_table = None

    for table in tables:
        if table_title in str(table):
            target_table = table
            break

    rows = target_table.find("tbody").find_all("tr")

    data = []

    for row in rows:
        col = row.find_all("td")
        if col:
            date = col[0].text.strip()
            revenue = col[1].text.strip().replace("$", "").replace(",", "")
            data.append({"Date": date, "Revenue": revenue})

    df = pd.DataFrame(data)

    df.dropna(inplace=True)
    df = df[df['Revenue'] != ""]

    return df