BMAD Opportunity Scan Prompt

Context: user agent `ba-self-dev-finance` with defaults:
- risk_tolerance: high
- investment_horizon: 3-6 months
- accounts: [IBKR]

Task:
Given a small universe of tickers and their recent market data, score each ticker for suitability for short-term (3-6 month) trading, prioritizing momentum and volatility for potential gains.

Filters to apply:
- Respect high risk tolerance (allow leveraged instruments if listed).
- Ensure suggested position sizing does not exceed 5% of capital per position unless otherwise requested.

Output format: JSON array with {ticker, score(0-1), rationale, suggested_size}
