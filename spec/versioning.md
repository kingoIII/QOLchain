# Versioning policy

- The `qol_version` field is intentionally locked to a fixed constant for each schema revision (e.g. `0.1.0`).
- New protocol versions MUST be introduced via a new schema file (e.g. `claim.song.schema.json` for v0.2.0) and accompanied by updated verifier rules.
- Existing claims issued under older schemas remain valid and should continue to be accepted by verifiers that support those versions.
- Verification implementations MUST inspect `qol_version` and apply the corresponding validation and canonicalization rules.
