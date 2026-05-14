from datetime import datetime, timedelta
from typing import Optional
import jwt

SECRET = "replace-with-secure-secret"
ALGO = "HS256"


def create_token(username: str, expires_minutes: int = 60) -> str:
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)}
    return jwt.encode(payload, SECRET, algorithm=ALGO)


def verify_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGO])
        return payload.get("sub")
    except Exception:
        return None
