from fastapi import FastAPI
from pydantic import BaseModel
from .scanner import scan_market

app = FastAPI(title="IBKR Opportunity Scanner")


class ScanRequest(BaseModel):
    universe: list[str] | None = None
    capital: float | None = None


@app.post("/scan")
def scan(req: ScanRequest):
    # Simple wrapper around scanner
    results = scan_market(universe=req.universe or ["AAPL", "TSLA", "SPY"], capital=req.capital or 1000)
    return {"count": len(results), "results": results}
