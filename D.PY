# This script creates a structured QOLchain Python base implementation
# and zips it so the user can download it directly.

import os
import zipfile
from pathlib import Path
import textwrap

base = Path("/mnt/data/qolchain_py")
base.mkdir(exist_ok=True)

structure = {
    "qolchain/__init__.py": "",
    "qolchain/canonical.py": """
import json, hashlib

def canonicalize(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

def hash_claim(obj):
    canon = canonicalize(obj)
    return hashlib.sha256(canon.encode()).hexdigest()
""",
    "qolchain/ledger.py": """
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
""",
    "qolchain/verify.py": """
from .canonical import hash_claim

def verify(claim):
    expected = hash_claim({k:v for k,v in claim.items() if k!="signature"})
    return claim.get("signature") == expected
""",
    "qolchain/anchor.py": """
def anchor(hash_value):
    print("ANCHOR PLACEHOLDER")
    print("Hash:", hash_value)
    print("Ethereum / Bitcoin adapters come next")
""",
    "main.py": """
import json, datetime, hashlib
from qolchain.canonical import hash_claim
from qolchain.ledger import append
from qolchain.verify import verify
from qolchain.anchor import anchor

claim = {
    "id": hashlib.sha256(str(datetime.datetime.utcnow()).encode()).hexdigest(),
    "type": "attestation",
    "issuer": "did:qol:issuer",
    "subject": input("Subject: "),
    "payload": {"note": input("Note: ")},
    "timestamp": datetime.datetime.utcnow().isoformat()
}

claim["signature"] = hash_claim({k:v for k,v in claim.items() if k!="signature"})

print("Verified:", verify(claim))
root = append(claim["signature"])
print("Merkle Root:", root)
anchor(claim["signature"])

with open("claim.json","w") as f:
    json.dump(claim,f,indent=2)
"""
}

for path, content in structure.items():
    full = base / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(textwrap.dedent(content).strip() + "\n")

zip_path = Path("/qolchain_python_base.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for file in base.rglob("*"):
        z.write(file, file.relative_to(base))

zip_path
