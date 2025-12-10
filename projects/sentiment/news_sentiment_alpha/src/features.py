import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def build_signal(prices: pd.DataFrame, news: pd.DataFrame, config: dict) -> pd.Series:
    if news.empty:
        return pd.Series(index=prices.index, data=0.0)

    # VADER on ALL headlines
    news["score"] = news["headline"].astype(str).apply(
        lambda x: analyzer.polarity_scores(x)["compound"]
    )
    
    # Print to verify
    print("📰 VADER scores:", news[["date", "headline", "score"]].to_dict('records'))
    
    # Filter weak signals (optional - comment out to use all)
    strong_news = news[abs(news["score"]) > 0.05]
    print(f"📰 Strong signals (|>0.05|): {len(strong_news)}/{len(news)}")
    
    if strong_news.empty:
        strong_news = news  # Fallback to all news
    
    grouped = strong_news.groupby("date")["score"].mean()
    signal = grouped.reindex(prices.index.date, method="ffill")
    signal.index = prices.index
    signal = signal.fillna(0.0)
    
    print(f"📊 Signal std: {signal.std():.3f}, non-zero days: {(signal != 0).sum()}")
    return signal

