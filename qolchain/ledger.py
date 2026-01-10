import json, hashlib
from pathlib import Path

LEDGER = Path("ledger.json")

def load():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {"claims": [], "roots": []}

def append(claim_hash):
    ledger = load()
    ledger["claims"].append(claim_hash)
    root = hashlib.sha256("".join(ledger["claims"]).encode()).hexdigest()
    ledger["roots"].append(root)
    LEDGER.write_text(json.dumps(ledger, indent=2))
    return root
