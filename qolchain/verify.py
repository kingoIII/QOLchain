from .canonical import hash_claim

def verify(claim):
    expected = hash_claim({k:v for k,v in claim.items() if k!="signature"})
    return claim.get("signature") == expected
