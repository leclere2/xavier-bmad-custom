IBKR Opportunity Scanner (prototype)

What this is
- Minimal prototype for a market-opportunity scanner tied to IBKR for execution.
- Uses a simple rule-based scanner and exposes a /scan endpoint to return candidate opportunities.

Structure
- `app/main.py` - FastAPI entrypoint
- `app/ibkr_connector.py` - IBKR connector stub (uses ib_insync when enabled)
- `app/scanner.py` - scanning logic (uses yfinance for market data in prototype)
- `prompts/scan_prompt.md` - BMAD-style prompt template that references `ba-self-dev-finance` defaults
- `config.example.env` - example environment variables

Security
- Never store real IBKR credentials in the repo. Use environment variables or a secrets manager.
- Start in paper trading mode for any real execution.

Run (local dev)
1) Create a Python venv and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Run server:

```bash
uvicorn app.main:app --reload --port 8001
```

3) Call the API:

```bash
curl -sS http://localhost:8001/scan | jq .
```

Next steps
- Wire `app/ibkr_connector.py` to real IBKR API credentials and enable paper trading.
- Plug BMAD prompts to the `prompts/scan_prompt.md` to use `ba-self-dev-finance` filters when scoring.
