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
