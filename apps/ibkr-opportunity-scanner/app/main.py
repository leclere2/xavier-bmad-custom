from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from .scanner import scan_market
from .auth import create_token, verify_token
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="IBKR Opportunity Scanner")

# serve frontend static files
static_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app.mount('/static', StaticFiles(directory=static_dir), name='static')


class ScanRequest(BaseModel):
    universe: list[str] | None = None
    capital: float | None = None


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post('/login')
def login(req: LoginRequest):
    # Prototype: accept any username/password; replace with real auth in prod
    token = create_token(req.username)
    return {"access_token": token}


def require_token(x_api_key: str | None = Header(None)) -> str:
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Missing token")
    user = verify_token(x_api_key)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user


@app.post("/scan")
def scan(req: ScanRequest, user: str = Header(None, alias="x-api-key")):
    # Validate token
    require_token(user)
    results = scan_market(universe=req.universe or ["AAPL", "TSLA", "SPY"], capital=req.capital or 1000)
    return {"count": len(results), "results": results}
