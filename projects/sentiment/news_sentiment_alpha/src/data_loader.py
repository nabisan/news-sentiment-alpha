# projects/sentiment/news-sentiment-alpha/src/data_loader.py

import pandas as pd
import yfinance as yf
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

FINVIZ_URL = "https://finviz.com/quote.ashx?t="

def fetch_news(tickers: list[str]) -> pd.DataFrame:
    records = []
    for ticker in tickers:
        url = FINVIZ_URL + ticker
        req = Request(url=url, headers={
            "User-Agent": "Mozilla/5.0"
        })
        html = BeautifulSoup(urlopen(req), "html.parser")
        news_table = html.find(id="news-table")
        if news_table is None:
            continue
        for row in news_table.find_all("tr"):
            a_tag = row.find("a")
            if not a_tag:
                continue
            headline = a_tag.get_text(strip=True)
            date_text = row.td.text.split()
            if len(date_text) == 2:
                date = date_text[0]
            else:
                # "Today" rows; skip for now or handle separately
                continue
            records.append({"ticker": ticker, "date": date, "headline": headline})
    df = pd.DataFrame(records)
    if df.empty:
        return df
    df["date"] = pd.to_datetime(df["date"], format="%b-%d-%y", errors="coerce").dt.date
    return df

def load_data(config: dict):
    tickers = config["universe"]
    start = config["start_date"]
    end = config["end_date"]

    prices = yf.download(tickers, start=start, end=end, auto_adjust=False)["Adj Close"]
    prices = prices.dropna(how="all")

    news = fetch_news(tickers)
    return prices, news

