from typing import Any

try:
    from ib_insync import IB
except Exception:
    IB = None


class IBKRConnector:
    def __init__(self, paper: bool = True):
        self.paper = paper
        self.ib = None

    def connect(self, host: str = "127.0.0.1", port: int = 7497, clientId: int = 1) -> bool:
        if IB is None:
            return False
        self.ib = IB()
        self.ib.connect(host, port, clientId)
        return self.ib.isConnected()

    def get_account_summary(self) -> dict[str, Any]:
        if not self.ib:
            return {"connected": False}
        # stub: replace with real calls
        return {"connected": True, "portfolio_value": 10000}

    def place_order(self, *args, **kwargs) -> dict:
        # Safety first: do not place real orders unless explicitly enabled.
        return {"ok": False, "reason": "Execution disabled in prototype"}
