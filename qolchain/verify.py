import os
import json
from .canonical import hash_claim


def _normalize_hex(s):
    if isinstance(s, str) and s.startswith("0x"):
        return s[2:]
    return s


def verify(claim):
    """Verify a claim or a signed-wrapper.

    Supported formats:
    - A claim dict with `signature` as a hex string (or without 0x prefix).
    - A claim dict with `signature` as a dict containing `signatureValue`.
    - A signed-wrapper with `claim_file` and `claim_hash` (verifies by loading the file and comparing hashes).
    """
    # Signed-wrapper: {"claim_file": "path/to/claim.json", "claim_hash": "0x...", ...}
    if isinstance(claim, dict) and 'claim_file' in claim and 'claim_hash' in claim:
        rel = claim['claim_file']
        candidates = []
        if os.path.isabs(rel):
            candidates.append(rel)
        else:
            candidates.append(os.path.join(os.getcwd(), rel))
            candidates.append(os.path.join(os.getcwd(), 'examples', rel))
            candidates.append(rel)
        c = None
        for p in candidates:
            try:
                c = json.load(open(p))
                break
            except Exception:
                continue
        if c is None:
            return False
        h = hash_claim(c)
        return _normalize_hex(h) == _normalize_hex(claim['claim_hash'])

    sig = claim.get('signature')

    # Signature is an object with signatureValue
    if isinstance(sig, dict):
        signature_value = sig.get('signatureValue')
        if signature_value:
            expected = hash_claim({k: v for k, v in claim.items() if k != 'signature'})
            return _normalize_hex(signature_value) == _normalize_hex(expected)
        return False

    # Signature is a simple string (hex)
    expected = hash_claim({k: v for k, v in claim.items() if k != 'signature'})
    return claim.get('signature') == expected or _normalize_hex(claim.get('signature')) == _normalize_hex(expected)
