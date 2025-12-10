import pandas as pd
from .metrics import compute_metrics

def run_backtest(prices: pd.DataFrame, signal: pd.Series, config: dict):
    signal = signal.reindex(prices.index).fillna(0)
    z = (signal - signal.mean()) / signal.std() if signal.std() != 0 else signal * 0
    positions = (z > 0).astype(float)

    rets = prices.pct_change().fillna(0)
    strat_rets = positions.shift(1).fillna(0) * rets

    equity = (1 + strat_rets).cumprod()
    summary = compute_metrics(strat_rets, equity)
    return summary, equity

