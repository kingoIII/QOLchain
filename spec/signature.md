# Signature (detached)

- Signatures MUST be detached from the claim JSON. The claim is pure semantic content and MUST NOT contain cryptographic envelopes.
- Recommended signature scheme: ECDSA over secp256k1 (compatible with Ethereum), but verifiers MAY accept other algorithms as long as they are documented.
- Signing procedure (recommended):
  1. Canonicalize the claim JSON according to RFC 8785 (see `canonicalization.md`).
  2. Hash the canonical bytes (e.g., keccak256 for Ethereum workflows).
  3. Sign the hash using the chosen algorithm and record signature metadata in a separate file or container.

Signed claim container example (`song.claim.signed.json`):

{
  "claim_file": "song.claim.json",
  "claim_hash": "0x...",
  "signature": {
    "type": "EcdsaSecp256k1",
    "created": "2026-01-02T12:01:00Z",
    "signatureValue": "0x...",
    "verificationMethod": "did:qol:creator:...#keys-1",
    "algorithm": "eth_sign"
  }
}

Notes:
- The `verificationMethod` SHOULD be a DID URL pointing to the key used to sign.
- Implementations MAY provide utilities to produce detached signature files or to package claim+signature in an archive; however, the authoritative claim payload remains the standalone JSON claim file.
