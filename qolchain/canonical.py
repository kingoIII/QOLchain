import json, hashlib

def canonicalize(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

def hash_claim(obj):
    canon = canonicalize(obj)
    return hashlib.sha256(canon.encode()).hexdigest()
