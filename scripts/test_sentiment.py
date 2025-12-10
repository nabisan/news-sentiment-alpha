import sys
from pathlib import Path
import yaml

print("DEBUG: top of test_sentiment.py reached")  # <- add this

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from projects.sentiment.news_sentiment_alpha.src import data_loader, features, backtest

def main():
    print("DEBUG: inside main()")  # <- add this

    config_path = ROOT / "projects" / "sentiment" / "news_sentiment_alpha" / "config.yaml"
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    print("✅ Config loaded")

    prices, news = data_loader.load_data(cfg)
    print("✅ Prices shape:", prices.shape)
    print("✅ News rows:", len(news))

    print("🔄 Building signal...")
    signal = features.build_signal(prices, news, cfg)
    print("✅ Signal created")

    print("🔄 Running backtest...")
    summary, equity = backtest.run_backtest(prices["AMZN"], signal, cfg)
    print("✅ Summary:", summary)

if __name__ == "__main__":
    print("DEBUG: __main__ reached, calling main()")  # <- add this
    main()

