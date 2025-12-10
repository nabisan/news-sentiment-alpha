import numpy as np
import pandas as pd

def compute_metrics(returns: pd.Series | pd.DataFrame, equity: pd.DataFrame):
    if isinstance(returns, pd.DataFrame):
        returns = returns.mean(axis=1)

    daily = returns.mean()
    vol = returns.std()
    sharpe = (daily / vol * np.sqrt(252)) if vol != 0 else 0.0
    max_dd = (equity / equity.cummax() - 1).min().min()
    ann_ret = (1 + daily) ** 252 - 1

    return {
        "annual_return": float(ann_ret),
        "sharpe": float(sharpe),
        "max_drawdown": float(max_dd),
    }

