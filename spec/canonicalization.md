# Canonicalization

This project uses a canonical JSON representation to ensure consistent hashing and signing.

- Reference: JSON Canonicalization Scheme (RFC 8785) — use the exact algorithm and ordering specified there.
- Procedure for signing/verifying:
  1. Serialize the claim JSON according to RFC 8785 canonicalization rules.
  2. Compute the hash of the resulting bytes (e.g., keccak256 for Ethereum workflows, or sha256 as needed).
  3. Use the hash as the message to sign with your chosen signature scheme.

Notes:
- Verifiers must implement the same canonicalization and hashing algorithm as the signer; mismatches will break signature verification.
- Canonicalization is separate from signing and must not modify the semantic content of the claim (no additional metadata injected into the claim).