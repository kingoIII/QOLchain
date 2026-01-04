import { keccak256 } from 'js-sha3';

// Minimal CLI to create a claim JSON and print its keccak256 hash
// Usage: ts-node scripts/createClaim.ts

const sampleClaim = {
  id: 'urn:uuid:1234',
  issuer: 'did:example:issuer',
  subject: 'did:example:subject',
  issuanceDate: new Date().toISOString(),
  claim: { score: 95 }
};

const payload = JSON.stringify(sampleClaim);
const hash = keccak256(payload);
console.log('Claim:', payload);
console.log('keccak256:', '0x' + hash);
