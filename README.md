# QOLchain (Scaffold)

This repository contains a lightweight scaffold for a QOL (Quality of Life) claim system.

Structure:
- `spec/` — JSON Schema and documentation for claims, canonicalization, signatures, and verification
  - `versioning.md`, `canonicalization.md`, `signature.md`, `verification.md`
- `examples/` — canonical claim examples and detached signature containers (e.g. `song.claim.json`, `song.claim.signed.json`)
- `contracts/` — Solidity contracts: `QOLAnchor`, `QOLClaimNFT`, `QOLSubToken`
- `scripts/` — helper scripts to create, sign, anchor and mint NFT for claims

Next steps:
1. Add tests and a deployment script.
2. Wire up OpenZeppelin dependencies in `package.json` and `hardhat`/`foundry` config.
3. Implement canonicalization utilities and reference implementations for detached signatures.
4. Create separate schema files for other entity types when needed (e.g. `claim.album.schema.json`).
