## Sentiment-Based Trading Strategies

1. **News Sentiment Alpha**  
   Repo: [`newssentimentalpha`](https://github.com/nabisan/news-sentiment-alpha)  
   - Uses daily news headlines and the VADER sentiment model to generate long/flat signals for equities (e.g., AMZN, TSLA, GOOG).
   - Aligns news with price data, builds a daily sentiment signal, and backtests it with annual return, Sharpe ratio, and max drawdown metrics.
   - Configurable via YAML for universe, date range, and trading parameters (holding period, transaction costs, benchmark).
