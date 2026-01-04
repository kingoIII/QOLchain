# Verification Steps

1. Validate claim JSON against `claim.schema.json`.
2. Recreate canonical payload and compute its hash (see `canonicalization.md`).
3. Verify the detached signature recovers the claimed signer and matches the referenced `claim_hash`.
4. Check on-chain anchor existence (if anchored) by querying `QOLAnchor`.
5. Optionally check revocation lists or status endpoints.

Additional verification rules:
- Contributor share validation: If `contributors` are present, the verifier MUST ensure the sum of `share` values is ≤ 10000 (basis points). Exact enforcement (equality vs inequality) is an application policy; verifiers MUST at least reject sums > 10000.
- License checks: Verifiers SHOULD confirm the `license` string matches known identifiers and apply any policy checks (e.g., non-commercial flags) as configured by the verifier.

Notes:
- Anchors and other post-issuance artifacts are not part of the claim; they are recorded in separate indexer or anchor records.
