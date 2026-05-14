import yfinance as yf
import pandas as pd


def simple_momentum_score(ticker: str) -> float:
    # Fetch 30d history and compute simple momentum (close / sma(10))
    data = yf.download(ticker, period="40d", progress=False)
    if data.empty:
        return 0.0
    close = data["Close"]
    sma10 = close.rolling(window=10).mean().iloc[-1]
    if pd.isna(sma10) or sma10 == 0:
        return 0.0
    return float((close.iloc[-1] / sma10) - 1)


def scan_market(universe: list[str], capital: float = 1000) -> list[dict]:
    results = []
    for t in universe:
        try:
            score = simple_momentum_score(t)
            results.append({"ticker": t, "score": score, "suggested_size": max(0, capital * 0.02)})
        except Exception:
            results.append({"ticker": t, "score": 0.0, "error": True})
    # sort by score desc
    results = sorted(results, key=lambda r: r.get("score", 0), reverse=True)
    return results
